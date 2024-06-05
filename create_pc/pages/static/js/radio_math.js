var price_content = document.querySelector('span#price').content;

function checked() {
    if(document.querySelector('input[type="radio"]:checked') !== null )
        {
            radioValue = document.getAttribute("data-simpletype-value").value;
            document.querySelector('span#price').content = price_content + radioValue;
            return price_content;
         }
}


//Я кароч хотел через атрибут дата забирать цену комплектующих, а потом суммировать в атребуте контент у id="price"
