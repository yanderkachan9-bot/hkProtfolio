function applyLanguage(lang) {
  document.querySelectorAll('[data-uk]').forEach(el => {
    el.textContent = lang === 'en' ? el.dataset.en : el.dataset.uk;
  });
  document.querySelectorAll('[data-uk-placeholder]').forEach(el => {
    el.placeholder = lang === 'en' ? el.dataset.enPlaceholder : el.dataset.ukPlaceholder;
  });
  document.querySelectorAll('.lang-uk').forEach(el => el.classList.toggle('active', lang === 'uk'));
  document.querySelectorAll('.lang-en').forEach(el => el.classList.toggle('active', lang === 'en'));

  localStorage.setItem('lang', lang);
}

document.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('lang') || 'uk';
  applyLanguage(saved);
});