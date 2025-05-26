
  const menuToggle = document.getElementById('menu-togle');
  const navLinks = document.getElementById('nav-link');

  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('show');
  });
