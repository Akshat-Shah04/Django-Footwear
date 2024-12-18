from django.db import models
from django.utils import timezone


class User(models.Model):

    ROLE_CHOICES = [
        ("buyer", "Buyer"),
        ("seller", "Seller"),
    ]

    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=20)
    profile = models.ImageField(
        upload_to="profile_images/", default="profile_images/default.jpg"
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="buyer")

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Running", "Running"),
        ("Casual", "Casual"),
        ("Formal", "Formal"),
        ("Sports", "Sports"),
        ("Sneakers", "Sneakers"),
    ]

    SIZE_CHOICES = [
        ("US 7", "US 7"),
        ("US 8", "US 8"),
        ("US 9", "US 9"),
        ("US 10", "US 10"),
        ("EU 40", "EU 40"),
        ("EU 42", "EU 42"),
    ]

    BRAND_CHOICES = [
        ("Nike", "Nike"),
        ("Adidas", "Adidas"),
        ("Puma", "Puma"),
        ("Reebok", "Reebok"),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)
    desc = models.TextField()
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    pimage = models.ImageField(upload_to="shoes/")

    def __str__(self):
        return f"{self.brand} {self.pname}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ttime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product} - Wishlist"


class Coupon(models.Model):
    code = models.CharField(max_length=15, unique=True)
    discount_value = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.discount_value}"

    @classmethod
    def add_default_coupons(cls):
        default_coupons = [
            {"code": "GET50", "discount_value": 50, "is_active": True},
            {"code": "DISCOUNT100", "discount_value": 100, "is_active": True},
            {"code": "GRAB20", "discount_value": 20, "is_active": True},
            {"code": "SAVE30", "discount_value": 30, "is_active": True},
            {"code": "FESTIVE25", "discount_value": 25, "is_active": True},
            {"code": "NEWUSER10", "discount_value": 10, "is_active": True},
            {"code": "SUMMER15", "discount_value": 15, "is_active": True},
            {"code": "WINTER20", "discount_value": 20, "is_active": True},
            {"code": "SPRING30", "discount_value": 30, "is_active": True},
            {"code": "WELCOME5", "discount_value": 5, "is_active": True},
            {"code": "SUMMERSALE", "discount_value": 25, "is_active": True},
        ]
        for coupon in default_coupons:
            cls.objects.get_or_create(
                code=coupon["code"],
                defaults={
                    "discount_value": coupon["discount_value"],
                    "is_active": coupon["is_active"],
                },
            )


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_date = models.DateTimeField(default=timezone.now)
    payment = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Cancelled", "Cancelled"),
        ("Delivered", "Delivered"),
        ("Shipping", "Shipping"),
        ("Ordered", "Ordered"),
        ("Paid", "Paid"),
        ("Saved", "Saved"),
    ]
    cart_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Active"
    )

    @property
    def subtotal(self):
        """Calculate the subtotal for all items in the cart for the same user."""
        cart_items = CartItem.objects.filter(cart=self)
        return sum(item.total for item in cart_items)

    @property
    def discount(self):
        if self.coupon and self.coupon.is_active:
            return self.coupon.discount_value
        return 0

    @property
    def delivery(self):
        cart_items = CartItem.objects.filter(cart=self)
        if not cart_items.exists():
            return 0
        return 50 if self.subtotal <= 500 else 0

    @property
    def roundtotal(self):
        """Calculate the final total after delivery charges and discounts."""
        return max(self.subtotal + self.delivery - self.discount, 0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product, related_name="cart_items", on_delete=models.CASCADE
    )
    qty = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.product.price * self.qty

    def __str__(self):
        return f"{self.qty} x {self.product.pname} (Cart Items)"


class Billing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Record creat
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Billing -> User {self.user.fname} {self.user.lname} -> {self.first_name} {self.last_name}"


class Order(models.Model):
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Order Confirmed", "Order Confirmed"),
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ("Out For Delivery", "Out For Delivery"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]
    order_number = models.CharField(max_length=25,unique=True)
    payment_method = models.CharField(max_length=20, editable=False, default="cod")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    order_total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)  # Record creat
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Order Confirmed"
    )

    @property
    def calculate_order_total(self):
        return self.cart.roundtotal

    def save(self, *args, **kwargs):
        """
        Override the save method to calculate and set the order total
        dynamically based on the cart.
        """
        self.order_total = self.calculate_order_total
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.fname} - {self.billing.city} - {self.order_total}"
