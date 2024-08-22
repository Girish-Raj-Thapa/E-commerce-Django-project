from django.urls import path 

from . import views

from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_view
from . forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:value>', views.CategoryView.as_view(), name='category'),
    path('category-title/<value>', views.CategoryTitleView.as_view(), name='category-title'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name="product-detail"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('update-address/<int:pk>', views.UpdateAddress.as_view(), name='update-address'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('paymentdone/', views.payment_done, name='payment_done'),
    path('orders/', views.orders, name='orders'),
    path('search/', views.search, name='search'),

    path('pluscart/', views.plus_cart, name='plus_cart'),
    path('minuscart/', views.minus_cart, name='minus_cart'),
    path('removecart', views.remove_cart, name='remove_cart'),

    path('showwishlist/', views.show_wishlist, name='show_wishlist'),
    path('pluswishlist/', views.plus_wishlist, name='plus_wishlist'),
    path('minuswishlist/', views.minus_wishlist, name='minus_wishlist'),


    # Customer Registration
    path('registration/', views.CustomerRegistrationView.as_view(), name='customer-registration'),
    # Login 
    path('account/login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    # Password Change
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='password-change'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    # Logout
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

     # Password reset
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)