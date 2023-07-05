import React from "react";
import "./Product.css";
import { useStateValue } from "./StateProvider";

function Product({id, title, image, price, rating}) {

    const [state, dispatch] = useStateValue(); // dispatch is alternate name for action

    const addToBasket = () => {
        dispatch({
            type: "ADD_TO_BASKET",
            item: {
                id: id,
                image: image,
                price: price,
                rating: rating,
            },
        });
    };

// JS variablies or objects have to be put in {}

    return (
        <div className="product">
            <div className="product__info"> 
                <p>{title}</p> 
                <p className="product__price">
                    <small>$</small>
                    <strong>{price}</strong>
                </p>
                <div className="product__rating">
                    {Array(rating) //making the rating dinamic as it is set by the rating key in the Home.js file
                    .fill() //filling the whole array
                    .map((_, i) => ( //the 2 parameters in the map array will be _ for each and every item and i for the integers
                        <p>⭐</p>
                    ))}
                </div>
            </div>

            <img src={image} />

            <button onClick={addToBasket}>Add to Basket</button>
        </div>
    )
}

export default Product