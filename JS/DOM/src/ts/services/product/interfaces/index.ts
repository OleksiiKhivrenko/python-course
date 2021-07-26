import {Nullable} from "../../../types";

export interface IProduct {
    id: number,
    category: string,
    imgUrl: string,
    name: string,
    display: Nullable<number>,
    color: string[],
    price: number,
    chip: Nullable<object>,
    ram: Nullable<number>,
    storage: Nullable<number>,
    touchId: boolean,
    faceId: boolean,
    wireless: string[],
    camera: Nullable<object>,
    audio: Nullable<object>,
    size: Nullable<object>,
    os: Nullable<string>,
    InTheBox?: string[],
    orderInfo?: object
}
