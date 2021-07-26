"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const items_1 = require("./items");
const product_1 = __importDefault(require("./product"));
require("./product");
const products = items_1.items.map(item => new product_1.default(item));
console.log(products[0].getItem());
//# sourceMappingURL=index.js.map