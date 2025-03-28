import { useReducer } from 'react';
import reducer from '../services/CartReducer';

function Cart() {

    const cart = [
        {
            id: 1,
            brand: "IKON FASHION",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20241109/0tsd/672e8ecbf9b8ef490b10254d/ikon_fashion_brown_solid_regular_fit_shirt.jpg",
            name: "Solid Regular Fit Shirt",
            price: 598,
            discount: 50,
            quantity: 1
        },
        {
            id: 2,
            brand: "U.S. Polo Assn.",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20250217/oxOi/67b33f4a2960820c4989d249/u.s._polo_assn._brown_men_slim_fit_polo_t-shirt_with_brand_print.jpg",
            name: "Men Slim Fit Polo T-Shirt",
            price: 900,
            discount: 50,
            quantity: 1
        },
        {
            id: 3,
            brand: "SIN",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20241025/fVmL/671ba52a260f9c41e89f6a7b/sin_indigo_men_heavy-wash_danzel_fit_jeans.jpg",
            name: "Men Heavy-Wash Danzel Fit Jeans",
            price: 598,
            discount: 50,
            quantity: 1
        },
        {
            id: 4,
            brand: "KOTTY",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20250117/EbZW/6789b063663dbe1c5fdd4164/kotty_cobalt_blue_men_cotton_jeans_.jpg",
            name: "Men Cotton Jeans ",
            price: 56,
            discount: 72,
            quantity: 1
        }
    ];

    const [ state, dispatch ] = useReducer(reducer, cart);

    console.log(state);
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
