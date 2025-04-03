import { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import axios from 'axios';

function Clothes() {
    const [clothes, setClothes] = useState([]);
    const [cart, setCart] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    let selectedCategories = [];
    const [filteredClothes, setFilteredClothes] = useState([]);

    const getDiscountedPrice = (cloth) => {
        return cloth.price - (cloth.price * cloth.discount / 100);
    };

    const addToCart = async (cloth) => {
        try {
            const requestBody = {
                brand: cloth.brand,
                name: cloth.name,
                quantity: 1,
                imageUrl: cloth.imageUrl,
                price: cloth.price,
                discount: cloth.discount,
                productId: cloth.id
            };
            const response = await axios.post('http://localhost:4000/cart', requestBody);
            window.alert('Added to cart');
            fetchClothes();
        } catch(error) {

        }
    }

    const removeCloth = async (cloth) => {
        try {
            const response = await axios.delete('http://localhost:4000/cart/' + cloth.cartId);
            window.alert('Removed cloth successfully');
            fetchClothes();
        } catch(error) {

        }
    }

    const updateQuantity = async (cloth) => {
        try {
            const requestBody = {
                quantity: cloth.quantity + 1
            };
            const response = await axios.patch('http://localhost:4000/cart/' + cloth.cartId, requestBody);
            window.alert('Updated cloth successfully');
            fetchClothes();
        } catch(error) {

        }
    }

    const fetchClothes = async () => {
        try {
            const response = await axios('http://localhost:4000/clothes');
            setClothes(response.data);
            setFilteredClothes(response.data);
            fetchCart(response.data);
        } catch(error) {

        }
    };

    const fetchCart = async (actualClothes) => {
        try {
            const response = await axios.get('http://localhost:4000/cart');

            const modifiedClothes = actualClothes.map(cloth => {
                const cartCloth = response.data.filter(cart => cart.productId === cloth.id);
                if (cartCloth && cartCloth.length > 0) {
                    return {...cloth, isClothInCart: true, quantity: cartCloth[0].quantity, cartId: cartCloth[0].id };
                } else {
                    return {...cloth, isClothInCart: false, quantity: 0 };
                }

            });

            setClothes(modifiedClothes);
            setFilteredClothes(modifiedClothes);

        } catch(error) {

        }
    };

    useEffect(() => {
        fetchClothes();
    }, []);

    const onSelectCategory = (category, checked) => {
        if (checked) {
            selectedCategories.push(category);
        } else {
            selectedCategories = selectedCategories.filter(_category => _category !== category);
        }

        console.log(selectedCategories);

        let filteredData = clothes.filter((cloth) => {
            if (selectedCategories.includes(cloth.category)) {
                return true;
            } else {
                return false;
            }
        });

        // if (selectedCategories.length === 0) {
        //     filteredData = [...clothes];
        // }
        
        console.log(filteredData);

        setFilteredClothes(filteredData);
    }
    useEffect(() => {
        const filteredData = clothes.filter((cloth) => cloth.brand.includes(searchQuery));

        setFilteredClothes(filteredData);
    }, [searchQuery]);

    return (
        <div>
            <h1 className="text-center text-4xl font-semibold my-8">Clothes</h1>
            <div className="flex px-10">
                <div className="w-1/4">
                    <div>
                        <p className="font-semibold">Gender</p>
                        <div>
                            <input type="checkbox" name="men" className="cursor-pointer" onChange={(event) => onSelectCategory('Men', event.target.checked)}/><span className="ms-2">Men</span>
                        </div>
                        <div>
                            <input type="checkbox" name="women" className="cursor-pointer" onChange={(event) => onSelectCategory('Women', event.target.checked)}/><span className="ms-2">Women</span>
                        </div>
                    </div>
                </div>
                <div className="w-3/4">
                    <div>
                        <input type="text" onChange={(event) => setSearchQuery(event.target.value)} placeholder="Enter Search Query..." className="border p-2 my-4 w-100 border-gray-200"/>
                    </div>
                    <div id="clothes" className="flex space-between gap-x-10 gap-y-10 mb-10 flex-wrap">
                        {filteredClothes?.map((cloth, index) => (
                            <div className="cloth text-center" key={cloth.id}>
                                <img src={cloth.imageUrl} className="w-80" />
                                <p className="font-semibold">{cloth.brand}</p>
                                <Link to={`/cloth-details/${cloth.id}?name=${cloth.name}&brand=${cloth.brand}`}><p>{cloth.name}</p></Link>
                                <p className="bg-green-400 w-30 mx-auto rounded-lg"><span className="me-1 border-r pe-1">{cloth.avgRating}</span><span>{cloth.ratingCount}</span></p>
                                <p><span className="font-semibold me-1">₹{getDiscountedPrice(cloth)}</span><span className="me-1">{cloth.price}</span><span>({cloth.discount} off)</span></p>
                                {cloth.isClothInCart ? (
                                    <div className="border border-gray-300 rounded-lg w-36 flex justify-between px-1 items-center mx-auto my-2">
                                        <i className="fa-solid fa-trash text-red-400 cursor-pointer" onClick={() => removeCloth(cloth)}></i>
                                        <span>{cloth.quantity}</span>
                                        <i className="fa-solid fa-plus text-blue-400 cursor-pointer" onClick={() => updateQuantity(cloth)}></i>
                                    </div>
                                ) : (
                                    <button onClick={() => addToCart(cloth)} className="bg-blue-500 text-white py-1 px-3 my-1 rounded-full cursor-pointer">Add to Cart</button>
                                )}
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )

}

export default Clothes;