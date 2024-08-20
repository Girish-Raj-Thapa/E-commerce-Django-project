<h1>E-commerce-Django-project</h1>

<h2>Overview</h2>

This Django project is a complete e-commerce solution that allows users to browse products, manage a shopping cart, place orders, and handle payments. It includes user authentication, profile management, and a wishlist feature.

<h2>Features</h2>
<ul>
  <li>Product Management: Users can view products by category or title.</li>
  <li>Shopping Cart: Users can add, update, or remove products from their cart.</li>
  <li>Checkout: Users can proceed to checkout and make payments using Razorpay (or eSewa, if updated).</li>
  <li>User Authentication: Registration, login, logout, and password management.</li>
  <li>Profile Management: Users can update their profile information and address.</li>
  <li>Wishlist: Users can add products to their wishlist.</li>
  <li>Admin Interface: Admins can manage the site from the Django admin interface.</li>
</ul>

<h2>Project Structure</h2>

<ul>
  <li>core/: Contains the main application for the e-commerce site, including models, views, and templates.
    <ul>
      <li>models.py: Defines the models for Product, Customer, Cart, Payment, OrderPlaced, and WishList.</li>
      <li>views.py: Contains views for handling product display, cart management, user registration, profile updates, and checkout.</li>
      <li>urls.py: Maps URLs to views.</li>
      <li>templates/: Contains HTML templates for the site.</li>
      <li>forms.py: Contains forms for user registration and profile updates.</li>
    </ul>
  </li>
</ul>

<h2>Setup</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3.x</li>
  <li>Django 5.0.6</li>
  <li>MySQL 8.x</li>
  <li>pipenv (for managing dependencies)</li>
</ul>

<h2>Installation</h2>

<ol>
  <li>
    <h4>Clone the repository:</h4>
    <pre><code>git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
</code></pre>
  </li>

  <li>
    <h4>Install dependencies:</h4>
    <pre><code>pipenv install
</code></pre>
  </li>

  <li>
    <h4>Set up the database:</h4>
    <pre><code>Ensure you have MySQL installed and running. Update the DATABASES settings in settings.py with your MySQL credentials.
</code></pre>
  </li>

  <li>
    <h4>Apply migrations:</h4>
    <pre><code>pipenv run python manage.py migrate
</code></pre>
  </li>

  <li>
    <h4>Run the development server:</h4>
    <pre><code>pipenv run python manage.py runserver
</code></pre>
  </li>

  <li>
    <h4>Access the site:</h4>
    <pre><code>Open your web browser and navigate to http://127.0.0.1:8000/.
</code></pre>
  </li>
</ol>

<h2>Configuration</h2>

<h3>Settings</h3>
<ul>
  <li><strong>SECRET_KEY:</strong> Keep this key secure in production. For local development, it is hard-coded.</li>
  <li><strong>DEBUG:</strong> Set to False in production.</li>
  <li><strong>ALLOWED_HOSTS:</strong> Configure this for your production environment.</li>
  <li><strong>DATABASES:</strong> Update the MySQL configuration according to your setup.</li>
  <li><strong>EMAIL_BACKEND:</strong> Configured to use the console backend for development.</li>
</ul>

<h3>Razorpay Integration</h3>
<ul>
  <li><strong>RAZOR_KEY_ID and RAZOR_KEY_SECRET:</strong> Update these values with your Razorpay credentials.</li>
</ul>

<h2>Sample Accounts</h2>
<ul>
  <li><strong>Superuser</strong>
    <ul>
      <li><strong>Username:</strong> admin</li>
      <li><strong>Password:</strong> admin@12345</li>
      <li><strong>Email:</strong> admin@shop.com</li>
    </ul>
  </li>
  <li><strong>User</strong>
    <ul>
      <li><strong>Username:</strong> Ram</li>
      <li><strong>Password:</strong> abcd@123</li>
      <li><strong>Email:</strong> ram@neel.com</li>
    </ul>
  </li>
</ul>

<h2>Usage</h2>
<ul>
  <li><strong>Homepage:</strong> Browse and search for products.</li>
  <li><strong>Product Details:</strong> View product details and add to cart.</li>
  <li><strong>Cart:</strong> View, update, or remove items from the cart.</li>
  <li><strong>Checkout:</strong> Proceed to checkout and make payments.</li>
  <li><strong>Profile:</strong> Register, update profile, and manage addresses.</li>
  <li><strong>Wishlist:</strong> Add products to your wishlist.</li>
</ul>

<h2>Testing</h2>

Run tests using:
pipenv run python manage.py test

<h2>Contributing</h2>
<ul>
  <li>Fork the repository.</li>
  <li>Create a new branch for your feature or bug fix.</li>
  <li>Make your changes.</li>
  <li>Commit and push your changes.</li>
  <li>Create a pull request.</li>
</ul>

<h2>License</h2>
<ul>
  <li>This project is licensed under the MIT License. See the LICENSE file for details.</li>
</ul>

<h2>Acknowledgements</h2>
<ul>
  <li><a href="https://docs.djangoproject.com/" target="_blank">Django Documentation</a></li>
  <li><a href="https://razorpay.com/docs/" target="_blank">Razorpay Documentation</a></li>
</ul>




