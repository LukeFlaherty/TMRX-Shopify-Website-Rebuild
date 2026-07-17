(() => {
  const body = document.body;
  const cartDrawer = document.querySelector('[data-cart-drawer]');
  const mobileMenu = document.querySelector('[data-mobile-menu]');
  const menuToggle = document.querySelector('[data-menu-toggle]');

  const setOpenState = (element, isOpen, className) => {
    if (!element) return;
    element.hidden = !isOpen;
    element.classList.toggle(className, isOpen);
    body.classList.toggle('tmrx-lock-scroll', isOpen);
  };

  document.querySelectorAll('[data-cart-open]').forEach((button) => {
    button.addEventListener('click', () => setOpenState(cartDrawer, true, 'is-open'));
  });

  document.querySelectorAll('[data-cart-close]').forEach((button) => {
    button.addEventListener('click', () => setOpenState(cartDrawer, false, 'is-open'));
  });

  if (menuToggle) {
    menuToggle.addEventListener('click', () => {
      const willOpen = !mobileMenu?.classList.contains('is-open');
      menuToggle.setAttribute('aria-expanded', String(willOpen));
      setOpenState(mobileMenu, willOpen, 'is-open');
    });
  }

  document.querySelectorAll('[data-menu-close]').forEach((button) => {
    button.addEventListener('click', () => {
      menuToggle?.setAttribute('aria-expanded', 'false');
      setOpenState(mobileMenu, false, 'is-open');
    });
  });

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    menuToggle?.setAttribute('aria-expanded', 'false');
    setOpenState(cartDrawer, false, 'is-open');
    setOpenState(mobileMenu, false, 'is-open');
  });
})();
