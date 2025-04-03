import { useReducer } from 'react';
import reducer from '../services/CartReducer';
import { useState, useEffect } from 'react';
import axios from 'axios';

function Cart() {

    const [ state, dispatch ] = useReducer(reducer, []);

    useEffect(() => {
        fetchCart();
    }, []);

    const fetchCart = async () => {
        try {
            const response = await axios.get('http://localhost:4000/cart');
            dispatch({ type: 'ADD', data: response.data });
        } catch(error) {

        }
    };

    return (
        <div class="max-w-5xl mx-auto bg-white p-6 shadow-md rounded-lg">
            <h2 class="text-2xl font-bold mb-6">Shopping Cart</h2>

            <div className="flex justify-between gap-x-5 items-center">
                <div class="space-y-6 w-2/3">
                    {state.map(cloth => (
                        <div class="flex items-center border-b pb-4">
                            <img src={cloth.imageUrl} alt="Basic Tee" class="w-24 h-24 object-cover rounded-md" />
                            <div class="ml-4 flex-1">
                                <h3 class="text-lg font-semibold">{cloth.brand}</h3>
                                <p class="text-gray-500">{cloth.name}</p>
                                <p class="text-gray-900 font-semibold">{cloth.price}</p>
                                <p class="text-green-600 text-sm flex items-center">✔ In stock</p>
                            </div>
                            <div class="flex items-center border rounded-md">
                                <button disabled={cloth.quantity === 1} class="px-3 py-1 text-gray-600 hover:text-black cursor-pointer" onClick={() => dispatch({ id: cloth.id, type: 'DECREMENT' })}>−</button>
                                <span class="px-4 py-1">{cloth.quantity}</span>
                                <button class="px-3 py-1 text-gray-600 hover:text-black cursor-pointer" onClick={() => dispatch({ id: cloth.id, type: 'INCREMENT' })}>+</button>
                            </div>
                            <button class="ml-4 text-gray-500 hover:text-red-500" onClick={() => dispatch({ id: cloth.id, type: 'REMOVE' })}>✖</button>
                        </div>
                    ))}

                </div>

                <div class="mt-8 bg-gray-100 p-6 rounded-lg w-1/3">
                    <h3 class="text-lg font-bold mb-4">Order Summary</h3>
                    <div class="flex justify-between text-gray-600">
                        <span>Subtotal</span>
                        <span>$64.00</span>
                    </div>
                    <div class="flex justify-between text-gray-600 mt-2">
                        <span>Shipping estimate</span>
                        <span>$5.00</span>
                    </div>
                    <div class="flex justify-between text-gray-600 mt-2">
                        <span>Tax estimate</span>
                        <span>$8.32</span>
                    </div>
                    <div class="flex justify-between font-bold text-gray-900 mt-4 text-lg">
                        <span>Order Total</span>
                        <span>$77.32</span>
                    </div>

                    <button class="w-full bg-indigo-600 text-white py-3 mt-4 rounded-md hover:bg-indigo-700">
                        Checkout
                    </button>
                </div>
            </div>
        </div>
    )
}

export default Cart;
