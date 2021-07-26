import { IProduct } from "./interfaces";

export default class Product {
    props: IProduct;

    constructor(props: IProduct) {
        this.props = props;
    }

    getProductInfo(): IProduct {
        return this.props
    }
}
