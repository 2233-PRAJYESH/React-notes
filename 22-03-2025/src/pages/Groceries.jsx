import { useState, useEffect } from 'react';
import axios from 'axios';

function Groceries() {
    const [categories, setCategories] = useState([]);
    const [groceries, setGroceries] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState('All');

    useEffect(() => {
        fetchGroceries();
    }, [selectedCategory]);

    const fetchGroceries = async () => {
        try {
            // const response = await fetch('http://localhost:4000/groceries' , { method: 'GET' });
            // const parsedResponse = await response.json();

            let params = {};
            if (selectedCategory !== 'All') {
                params.category = selectedCategory;
            }

            const response = await axios.get('http://localhost:4000/groceries', { params: params });

            console.log(response.data);

            const temp = [];

            response.data.forEach(grocery => {
                if (!temp.includes(grocery.category)) {
                    temp.push(grocery.category);
                }
            });
            setCategories(['All', ...temp]);

            setGroceries(response.data);

        } catch (error) {

        }

    };

    const onSelectCategory = (category) => {
        console.log(category);
        setSelectedCategory(category);
    }

    return (
        <div className='px-20'>
            <h1 className='text-3xl text-center my-4'>Groceries</h1>

            <div className='flex'>
                <div className='w-1/4'>
                    {categories.map(category => (
                        <div className='p-3 shadow my-2 cursor-pointer' onClick={() => onSelectCategory(category)}>
                            <p className='text-lg font-semibold'>{category}</p>
                        </div>
                    ))}
                </div>
                <div className='w-3/4'>
                    <div className='flex flex-wrap gap-x-10 gap-y-10 space-between'>
                    {groceries.map(grocery => (
                        <div className="w-52 bg-white shadow-md rounded-lg p-4">
                            {/* Discount Badge */}
                            <div className="relative">
                                <span className="absolute top-0 left-0 bg-purple-700 text-white text-xs font-bold px-2 py-1 rounded-br-lg">
                                    {grocery.discount}
                                </span>
                                <img
                                    src="https://via.placeholder.com/150"
                                    alt="Assorted Roses"
                                    className="w-full h-32 object-cover rounded-lg"
                                />
                            </div>

                            {/* Product Info */}
                            <div className="mt-3">
                                <h3 className="text-gray-800 font-semibold">{grocery.name}</h3>
                                <p className="text-gray-500 text-sm">{grocery.weight}</p>

                                {/* Price Section */}
                                <div className="flex items-center space-x-2 mt-1">
                                    <span className="text-lg font-bold text-gray-900">₹{grocery.price}</span>
                                    <span className="text-sm text-gray-500 line-through">₹{grocery.orginalPrice}</span>
                                </div>

                                {/* Add to Cart Button */}
                                <button className="mt-3 w-full text-red-600 border border-red-600 py-2 rounded-md font-medium hover:bg-red-600 hover:text-white transition">
                                    Add to Cart
                                </button>
                            </div>
                        </div>
                    ))}
                    </div>
                </div>
            </div>

        </div>
    )

}

export default Groceries;