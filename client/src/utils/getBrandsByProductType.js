import { shirtBrands, jacketBrands, dressBrands } from "../data/brands";

export const getBrandsByProductType = (productType) => {
    switch(productType){
        case('shirt'):
            return shirtBrands;
        case('dress'):
            return dressBrands;
        case('jacket'):
            return jacketBrands;
        default:
            return []
    }
}