from pyscript import document, window

def apply_landscape_styles():
    document.body.classList.remove('phone')
    document.body.classList.add('desktop')

def apply_portrait_styles():
    document.body.classList.remove('desktop')
    document.body.classList.add('phone')

def show_content():
    element = document.querySelector('.main-grid')
    element.style.display = 'grid'

def check_screen_dimensions():
    if window.innerWidth > window.innerHeight:
        apply_landscape_styles()
    else:
        apply_portrait_styles()
    loading_screen = document.querySelector('.loading-screen')
    loading_screen.classList.add('hidden')
    loading_screen.addEventListener('transitionend', lambda event: loading_screen.parentNode.removeChild(loading_screen))
    show_content()

check_screen_dimensions()
