from pyscript import document, window

# Function to apply landscape styles
def apply_landscape_styles():
    # Replace this with your landscape styles
    document.body.classList.remove('phone')
    document.body.classList.add('desktop')
    show_content()

# Function to apply portrait styles
def apply_portrait_styles():
    # Replace this with your portrait styles
    document.body.classList.remove('desktop')
    document.body.classList.add('phone')
    show_content()

# Function to show the content
def show_content():
    # Select and show the content elements
    element = document.querySelector('.main-grid')
    element.style.display = 'grid'

# Check screen dimensions
def check_screen_dimensions():
    if window.innerWidth > window.innerHeight:
        # Landscape orientation
        apply_landscape_styles()
    else:
        # Portrait orientation
        apply_portrait_styles()

check_screen_dimensions()
