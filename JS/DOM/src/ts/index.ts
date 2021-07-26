import {items} from "./data/items";
import Product from "./services/product";


function renderProducts() {
    const productsContainer = document.querySelector('.products') as HTMLDivElement;
    const products = items.map(item => new Product(item));
    const productsHTML: string = products.reduce((str, product) => {
        const {name} = product.getProductInfo();

        return str + `<div class="product"><div class="name">${name}</div></div>`
    }, "")

    productsContainer.innerHTML = productsHTML;
}

renderProducts();




