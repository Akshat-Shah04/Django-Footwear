from django.shortcuts import render, redirect
import random
from .models import *
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
import os
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        # Get form data
        print("ERROR 1")
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        msg = request.POST["message"]
        print("ERROR 2")

        # Format the email subject and body
        email_subject = f"New Message from {fname} {lname} regarding {subject}"
        email_body = f"Name: {fname} {lname}\nEmail: {email}\nMessage: {msg}"

        try:
            # Send email to admin (recipient can be hardcoded or fetched from settings)
            print("ERROR 3")

            send_mail(
                email_subject,
                email_body,
                email,  # The user's email address is the sender
                [
                    os.getenv("ADMIN_EMAIL")
                ],  # Admin's email is the recipient, fetched from environment variable
                fail_silently=False,
            )
            print("ERROR 4")

            messages.success(request, "Your message has been sent successfully!")
            print("ERROR 5")

            return redirect("index")  # Redirect to contact page after success
        except Exception as e:
            print("ERROR 6")

            messages.error(request, f"Email sending failed: {e}")
            return redirect("contact")  # Redirect to contact page on failure
    else:
        # Handle GET request by rendering the contact form
        print("ERROR 7")

        return render(request, "contact.html")


def productDetails(request):
    return render(request, "productDetails.html")


def orderComplete(request):
    return render(request, "orderComplete.html")


def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST["email"])
            if user.password == request.POST["password"]:
                request.session["email"] = user.email
                request.session["profile"] = user.profile.url
                print("Login Successfully!!!")
                #                 send_mail(
                #                     "Thank You for Using Our Application",
                #                     f"""Dear {user.fname} {user.lname},

                # We sincerely thank you for choosing our application. We appreciate your trust in us and look forward to serving you.

                # If you have any questions or feedback, please feel free to reach out.

                # Best regards,
                # Akshat Shah
                # Developer""",
                #                     os.getenv("EMAIL_HOST_USER"),  # From email address
                #                     [user.email],  # Recipient email address
                #                     fail_silently=False,
                #                 )
                if user.role == "buyer":
                    return redirect("index")
                elif user.role == "seller":
                    return redirect("sindex")
                else:
                    return redirect("login")

            else:
                msgAlert = "Invalid Credentials !!!"
                return render(request, "login.html", {"msgAlert": msgAlert})
        except:
            msgAlert = "Login Failed!!!"
            return render(request, "login.html", {"msgAlert": msgAlert})
    else:
        return render(request, "login.html")


def logout(request):
    auth_logout(request)
    return redirect("login")


def signup(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST["email"])
            msgAlert = "Account already exists!!!"
            return render(request, "login.html", {"msgAlert": msgAlert})

        except:
            if request.POST["password"] == request.POST["cpassword"]:
                user = User.objects.create(
                    fname=request.POST["fname"],
                    lname=request.POST["lname"],
                    mobile=request.POST["mobile"],
                    email=request.POST["email"],
                    profile=request.FILES.get("profile"),
                    password=request.POST["password"],
                )

                msgSuccess = "Signup Successful!!"
                #                 send_mail(
                #                     "Thank You for Using Our Application",
                #                     f"""Dear {user.fname} {user.lname},

                # We sincerely thank you for choosing our application. We appreciate your trust in us and look forward to serving you.

                # If you have any questions or feedback, please feel free to reach out.

                # Best regards,
                # Akshat Shah
                # Developer""",
                #                     os.getenv("EMAIL_HOST_USER"),  # From email address
                #                     [user.email],  # Recipient email address
                #                     fail_silently=False,
                #                 )
                return render(request, "login.html", {"msgSuccess": msgSuccess})
            else:
                msgAlert = "Password and Confirm Password do not match!!!"
                return render(request, "signup.html", {"msgAlert": msgAlert})

    else:
        return render(request, "signup.html")


def cpass(request):
    if request.method == "POST":

        try:
            user = User.objects.get(email=request.session["email"])

            if request.POST["opassword"] == user.password:
                if request.POST["npassword"] == request.POST["cnpassword"]:
                    user.password = request.POST["npassword"]
                    user.save()
                    del request.session["email"]
                    return redirect("logout")
                else:
                    msgAlert = "New password and confirm password do not match!"
                    return render(
                        request,
                        "cpass.html",
                        {"msgAlert": msgAlert},
                    )
            else:
                msgAlert = "Old password does not match!"

                return render(request, "cpass.html", {"msgAlert": msgAlert})
        except User.DoesNotExist:
            msgAlert = "User not found!"
            return render(request, "cpass.html", {"msgAlert": msgAlert})
        except Exception as e:
            msgAlert = f"An error occurred: {str(e)}"
            return render(request, "cpass.html", {"msgAlert": msgAlert})
    else:
        return render(request, "cpass.html")


def scpass(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.session["email"])

            if request.POST["opassword"] == user.password:
                if request.POST["npassword"] == request.POST["cnpassword"]:
                    user.password = request.POST["npassword"]
                    user.save()
                    del request.session["email"]
                    return redirect("logout")
                else:
                    msgAlert = "New password and confirm password do not match!"
                    return render(
                        request,
                        "scpass.html",
                        {"msgAlert": msgAlert},
                    )
            else:
                msgAlert = "Old password does not match!"

                return render(request, "scpass.html", {"msgAlert": msgAlert})
        except User.DoesNotExist:
            msgAlert = "User not found!"
            return render(request, "scpass.html", {"msgAlert": msgAlert})
        except Exception as e:
            msgAlert = f"An error occurred: {str(e)}"
            return render(request, "scpass.html", {"msgAlert": msgAlert})
    else:
        return render(request, "scpass.html")


def generate_otp():
    """Generate a random 4-digit OTP."""
    return random.randint(1000, 9999)


def fpass(request):
    if request.method == "POST":
        email = request.POST.get("email")  # Get the email from the form
        try:
            # Try to get the user by email address
            user = User.objects.get(email=email)

            # Generate OTP
            otp = generate_otp()

            # Send OTP via email
            send_mail(
                "Your OTP Code",
                f"Your OTP code is {otp}.",
                os.getenv("EMAIL_HOST_USER"),  # From email address
                [user.email],  # Recipient email address
                fail_silently=False,
            )

            # Store the OTP and email in the session for later verification
            request.session["otp"] = otp
            request.session["email"] = user.email  # Store email in session

            return render(request, "otp.html")  # Redirect to OTP page

        except ObjectDoesNotExist:
            # Handle case where the email address is not registered
            msgAlert = "Email address not registered!!"
            return render(request, "fpass.html", {"msgAlert": msgAlert})
        except Exception as e:
            # Handle any other exceptions
            msgAlert = f"An error occurred: {str(e)}"
            return render(request, "fpass.html", {"msgAlert": msgAlert})

    else:
        return render(request, "fpass.html")


def otp(request):
    if request.method == "POST":
        # Check if OTP exists in the session
        if "otp" not in request.session or "email" not in request.session:
            msgAlert = "Session expired. Please request a new OTP."
            return render(request, "otp.html", {"msgAlert": msgAlert})

        try:
            # Get the OTP from the session and the user input
            otp = int(request.session["otp"])
            uotp = int(request.POST.get("uotp"))

            # Validate user input OTP
            if uotp == otp:
                del request.session["otp"]  # Clear OTP from session
                # del request.session["email"]  # Clear email from session
                return render(request, "newpass.html")  # Proceed to new password page
            else:
                msgAlert = "Invalid OTP!!!"
                return render(request, "otp.html", {"msgAlert": msgAlert})
        except ValueError:
            # Handle case where the user input is not an integer
            msgAlert = "Please enter a valid OTP!"
            return render(request, "otp.html", {"msgAlert": msgAlert})
        except Exception as e:
            # Handle any other exceptions
            msgAlert = f"An error occurred: {str(e)}"
            return render(request, "otp.html", {"msgAlert": msgAlert})
    else:
        # If not POST request, redirect to OTP page
        return render(request, "otp.html")


def newpass(request):
    if request.method == "POST":
        print(">>>>>>>>>>>>>>>>>>err1")

        try:
            email = request.session.get("email")
            if not email:
                raise Exception("No user logged in...")
            print(">>>>>>>>>>>>>>>>>>err2")
            if request.POST["npassword"] == request.POST["cnpassword"]:
                user = User.objects.get(email=email)
                user.password = request.POST["npassword"]
                print(">>>>>>>>>>>>>>>>>>err3")
                user.save()

                msgSuccess = "Password updated successfully!"
                print(">>>>>>>>>>>>>>>>>>err4")
                #                 send_mail(
                #                     "Security Alert : Password Update Notification",
                #                     f"""Dear {user.fname} {user.lname},

                # We would like to inform you that your password has been successfully updated.

                # If you did not initiate this change, please contact our support team immediately to secure your account.

                # If you did update your password, please disregard this message.

                # Thank you for your attention to this matter.

                # Best regards,
                # Akshat Shah
                # Developer""",
                #                     os.getenv("EMAIL_HOST_USER"),  # From email address
                #                     [user.email],  # Recipient email address
                #                     fail_silently=False,
                #                 )

                return redirect(login)

            else:
                msgAlert = "Password and Confirm New Password do not match!"
                return render(request, "newpass.html", {"msgAlert": msgAlert})

        except Exception as e:
            msgAlert = f"An error occurred: {str(e)}"
            print(str(e))
            return render(request, "newpass.html", {"msgAlert": msgAlert})

    else:
        return render(request, "newpass.html")


def profile(request):

    if "email" not in request.session:
        return redirect("login")

    try:
        user = User.objects.get(email=request.session["email"])

        if request.method == "POST":
            user.fname = request.POST.get("fname", user.fname)
            user.lname = request.POST.get("lname", user.lname)
            user.email = request.POST.get("email", user.email)
            user.mobile = request.POST.get("mobile", user.mobile)
            print("user : ", user.fname, ",", user.lname)
            if "profile" in request.FILES:
                user.profile = request.FILES["profile"]
            user.save()

            request.session["profile"] = user.profile.url
            print(user.profile.url)
            print("Updated Successfully...")

            send_mail(
                "Profile Update",
                f"""Dear {user.fname} {user.lname},\n\n
We would like to inform you that your profile has been successfully updated. 
If you did not initiate this change, please contact our support team immediately to secure your account.\n
If you did update your profile, please disregard this message.\n
Thank you for your attention to this matter.\n
Thank you for using this website.\n
Best regards,\n
Akshat Shah\n
Developer""",
                os.getenv("EMAIL_HOST_USER"),
                [user.email],
                fail_silently=False,
            )

            msgSuccess = "User Updated Successfully!!"
            print("User Updated Successfully!!!")

            return render(
                request, "index.html", {"msgSuccess": msgSuccess, "user": user}
            )

        return render(
            request, "profile.html", {"user": user}
        )  # Render profile template on GET

    except ObjectDoesNotExist:
        msgAlert = "User not found!"
        return render(request, "login.html", {"msgAlert": msgAlert})

    except Exception as e:
        print(f"Error: {e}")
        msgAlert = "An error occurred while updating your profile."
        return render(request, "profile.html", {"msgAlert": msgAlert})


def sindex(request):
    return render(request, "sindex.html")


def add(request):
    if request.method == "POST":
        try:
            email = request.session.get("email")
            if not email:
                msgAlert = "User not logged in!!"
                return render(request, "add.html", {"msgAlert": msgAlert})

            seller = User.objects.get(email=email)

            Product.objects.create(
                seller=seller,
                category=request.POST["category"],
                size=request.POST["size"],
                price=request.POST["price"],
                pname=request.POST["pname"],
                desc=request.POST["desc"],
                pimage=request.FILES["pimage"],
                brand=request.POST["brand"],
            )

            msgSuccess = "Product Added Successfully!!!"
            print("Product added!!")
            return render(request, "sindex.html", {"msgSuccess": msgSuccess})

        except User.DoesNotExist:
            msgAlert = "Seller not found!"
            print(">>>>>>> Exception >>>>>>>>> Seller not found")
            return render(request, "add.html", {"msgAlert": msgAlert})

        except Exception as e:
            msgAlert = "Product Not Created!!"
            print(">>>>>>> Exception >>>>>>>>>", e)
            return render(request, "add.html", {"msgAlert": msgAlert})

    else:
        return render(request, "add.html")


def viewProduct(request):
    seller = User.objects.get(email=request.session["email"])
    product = Product.objects.filter(seller=seller)
    return render(request, "viewProduct.html", {"product": product})


def updateProduct(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == "POST":
        try:
            seller = User.objects.get(email=request.session["email"])
            product.pname = request.POST.get("pname")
            product.price = request.POST.get("price")
            product.category = request.POST.get("category")
            product.size = request.POST.get("size")
            product.brand = request.POST.get("brand")
            product.desc = request.POST.get("desc")
            if "pimage" in request.FILES:
                product.pimage = request.FILES["pimage"]
            product.save()  # Save the updated product
            print("Product Edited...")
            return redirect("viewProduct")

        except Exception as e:
            print(">>>>>>>>>>> Exception >>>>>>>>>> ", e)
            return render(request, "sindex.html", {"msgAlert": str(e)})

    return render(request, "updateProduct.html", {"product": product})


def deleteProd(request, pk):
    product = Product.objects.filter(pk=pk)
    product.delete()
    print(">>>>>>>>>>>> Product Deleted >>>>>>>>>>>>")
    return redirect("viewProduct")


def wishlist(request):
    user = User.objects.get(email=request.session["email"])
    wishlist = Wishlist.objects.filter(user=user)
    return render(request, "wishlist.html", {"wish": wishlist})


def addwish(request, pk):
    user = User.objects.get(email=request.session["email"])
    product = Product.objects.get(pk=pk)
    if not Wishlist.objects.filter(user=user, product=product).exists():
        Wishlist.objects.create(user=user, product=product)
    return redirect("men")


def deletewish(request, pk):
    user = User.objects.get(email=request.session["email"])
    product = Product.objects.get(pk=pk)
    wish = Wishlist.objects.filter(user=user, product=product)
    wish.delete()
    print(">" * 30, "Product Deleted from wishlist", "<" * 20)

    return redirect("wishlist")


def cart(request):
    try:
        user = User.objects.get(email=request.session["email"])

        cart = Cart.objects.filter(user=user, cart_status="Active").first()

        if not cart:
            msg = "Your cart is empty. Add items to the cart."
            return render(request, "cart.html", {"msg": msg})

        cart_items = cart.items.all()  # Get cart items
        return render(
            request,
            "cart.html",
            {
                "cart": cart,
                "cart_items": cart_items,
                "subtotal": cart.subtotal,
                "delivery": cart.delivery,
                "roundtotal": cart.roundtotal,
                "msg": None,
            },
        )
    except User.DoesNotExist:
        messages.error(request, "User not found. Please log in.")
        return redirect("login")


def addcart(request, pk):
    user = User.objects.get(email=request.session["email"])
    product = Product.objects.get(pk=pk)

    # Ensure there's only one active cart for the user
    cart, created = Cart.objects.get_or_create(user=user, cart_status="Active")

    # Add product to the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.qty += 1  # Increment quantity if the item already exists
    cart_item.save()
    cart.save()

    return redirect("cart")


def applycoupon(request):
    if request.method == "POST":
        code = request.POST.get("code", "").strip()
        user = User.objects.get(email=request.session["email"])
        cart = Cart.objects.filter(user=user, payment=False).first()
        if not cart:
            messages.error(request, "You don't have an active cart.")
            return redirect("cart")

        # Check if the coupon exists and is active
        try:
            coupon = Coupon.objects.get(code=code, is_active=True)
            cart.coupon = coupon
            cart.save()

            request.session["applied_coupon"] = coupon.code
            request.session["discount"] = coupon.discount_value

            messages.success(request, f"Coupon '{coupon.code}' applied successfully!")

        except Coupon.DoesNotExist:
            messages.error(request, "Invalid or inactive coupon code.")

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

        return redirect("cart")

    messages.error(request, "Invalid request method.")
    return redirect("cart")


def cancelcoupon(request):
    del request.session["applied_coupon"]
    del request.session["discount"]
    return redirect("cart")


def changeqty(request, pk):
    if request.method == "POST":
        cart_item = CartItem.objects.filter(pk=pk).first()

        if cart_item is None:
            return redirect("cart")

        try:
            new_qty = int(request.POST.get("qty", 1))
            if new_qty < 1:
                new_qty = 1
            elif new_qty > 10:
                new_qty = 10
            cart_item.qty = new_qty
            cart_item.save()

            return redirect("cart")

        except ValueError:
            return redirect("cart")

    return redirect("cart")


def deletecart(request, pk):
    try:
        user = User.objects.get(email=request.session["email"])
        product = Product.objects.get(pk=pk)
        print("***** Step 1: Product fetched")

        cart_item = CartItem.objects.filter(product=product)
        print(f"***** Step 2: Cart items found: {cart_item.count()}")

        if cart_item.exists():
            print(f"***** Step 3: Found {cart_item.count()} cart item(s) to delete")
            cart_item.delete()
            messages.success(request, "Item removed from your cart.")
        else:
            print("***** Step 4: No matching cart item found.")
            messages.error(request, "Item not found in your cart.")

    except Exception as e:
        print(f"***** Error: {str(e)}")
        messages.error(request, "Error Caught")

    return redirect("cart")


def men(request):
    user = User.objects.get(email=request.session["email"])
    product = Product.objects.all()
    wish_ids = Wishlist.objects.filter(user=user).values_list("product_id", flat=True)
    return render(request, "men.html", {"product": product, "wish_ids": wish_ids})


def checkout(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        messages.error(request, "Cart not found.")
        return redirect("cart")

    cart_items = CartItem.objects.filter(cart=cart)
    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect("cart")

    subtotal = cart.subtotal
    discount = cart.discount
    delivery = cart.delivery
    roundtotal = cart.roundtotal

    return render(
        request,
        "checkout.html",
        {
            "cart": cart,
            "cart_items": cart_items,
            "subtotal": subtotal,
            "discount": discount,
            "delivery": delivery,
            "roundtotal": roundtotal,
        },
    )


def create_order(request, pk):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.session.get("email"))
            billing = Billing.objects.create(
                user=user,
                firstname=request.POST.get("firstname"),
                lastname=request.POST.get("lastname"),
                address=request.POST.get("address"),
                city=request.POST.get("city"),
                zipcode=request.POST.get("zipcode"),
                country=request.POST.get("country"),
                mobile=request.POST.get("mobile"),
            )

            cart = Cart.objects.get(pk=pk)
            cart_items = CartItem.objects.filter(cart=cart)
            print(cart)
            print(cart_items)
            if not cart_items.exists():  # Check if the cart is empty
                print("Cart is empty.")
                return redirect("cart")

            n = random.randint(1000000000, 9999999999)
            order_number = f"FW-{n}"
            print(">>>>>>>>>>>erroer2")

            order = Order.objects.create(
                order_number=order_number,
                user=user,
                cart=cart,
                billing=billing,
            )
            cart.cart_status = "Ordered"
            cart.save()
            print(">>>>>>>>>>>erroer1")
            return redirect(reverse("success"))

        except User.DoesNotExist:
            print(">>>>>>>>>>>erroer3")

            messages.error(request, "User not found.")
            return redirect("cart")

        except Cart.DoesNotExist:
            messages.error(request, "Cart not found.")
            return redirect("cart")

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            print(">>>>>>>>>>>erroer4")
            print(e)

            return redirect("cart")

    else:
        # If method is GET, just render the checkout page
        messages.error(request, "Invalid request method.")
        return redirect("cart")


def success(request):
    user = User.objects.get(email=request.session["email"])
    cart = Cart.objects.get(user=user)
    order = Order.objects.get(user=user, cart=cart)
    return render(request, "success.html", {"order": order})


def error(request):
    return render(request, "error.html")
