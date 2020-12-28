//функция для полной загрузки страницы
var ready = (callback) => {
    if (document.readyState != "loading") callback();
    else document.addEventListener("DOMContentLoaded", callback);
}

/*  Начинаем работу после полной загрузки DOM */
ready(() => {
  //Блок, сворачивающий/разворачивающий аккордеон. Без анимации.
  [].forEach.call(document.querySelectorAll('.faq_item_title_inner'), function (el) {
    el.addEventListener('click', function () {
      var faqItem = el.parentElement.parentElement;
      var itemBody = faqItem.querySelector('.faq_item_body');
      if (itemBody.style.display == "block") {
        itemBody.style.display = "none";
      } else itemBody.style.display = "block";
      el.classList.toggle("open");
    }, false);
  });
})
