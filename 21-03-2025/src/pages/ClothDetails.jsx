import { useParams, useSearchParams } from "react-router-dom";
import { useEffect, useState } from 'react';
import './ClothDetails.css';

function ClothDetails() {
    const params = useParams();
    const [searchParams, setSearchParams] = useSearchParams();
    let clothes = [
        {
            id: 1,
            brand: "IKON FASHION",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20241109/0tsd/672e8ecbf9b8ef490b10254d/ikon_fashion_brown_solid_regular_fit_shirt.jpg",
            name: "Solid Regular Fit Shirt",
            avgRating: 3.3,
            ratingCount: 4000,
            price: 598,
            discount: 50,
            category: 'Men'
        },
        {
            id: 2,
            brand: "U.S. Polo Assn.",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20250217/oxOi/67b33f4a2960820c4989d249/u.s._polo_assn._brown_men_slim_fit_polo_t-shirt_with_brand_print.jpg",
            name: "Men Slim Fit Polo T-Shirt",
            avgRating: 5,
            ratingCount: 2,
            price: 900,
            discount: 50,
            category: 'Men'
        },
        {
            id: 3,
            brand: "SIN",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20241025/fVmL/671ba52a260f9c41e89f6a7b/sin_indigo_men_heavy-wash_danzel_fit_jeans.jpg",
            name: "Men Heavy-Wash Danzel Fit Jeans",
            avgRating: 3.3,
            ratingCount: 4000,
            price: 598,
            discount: 50,
            category: 'Men'
        },
        {
            id: 4,
            brand: "KOTTY",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20250117/EbZW/6789b063663dbe1c5fdd4164/kotty_cobalt_blue_men_cotton_jeans_.jpg",
            name: "Men Cotton Jeans ",
            avgRating: 3.6,
            ratingCount: 500,
            price: 56,
            discount: 72,
            category: 'Men'
        },
        {
            id: 5,
            brand: "LEVIS",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20250107/cLEc/677d315c663dbe1c5fc2de89/levis_black_men_lightly_washed_511_slim_fit_jeans.jpg",
            name: "Men Lightly Washed 511 Slim Fit Jeans",
            avgRating: 4.5,
            ratingCount: 4000,
            price: 1450,
            discount: 50,
            category: 'Men'
        },
        {
            id: 6,
            brand: "POSHAX",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20241115/Iec6/673760320f47f80c878b0f4b/poshax_green_men_relaxed_fit_cargo_pants_with_insert_pockets.jpg",
            name: "Men Relaxed Fit Cargo Pants",
            avgRating: 3.6,
            ratingCount: 2000,
            price: 400,
            discount: 76,
            category: 'Men'
        },
        {
            id: 7,
            brand: "IKON FASHION",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20241109/0tsd/672e8ecbf9b8ef490b10254d/ikon_fashion_brown_solid_regular_fit_shirt.jpg",
            name: "Solid Regular Fit Shirt",
            avgRating: 3.3,
            ratingCount: 4000,
            price: 598,
            discount: 50,
            category: 'Men'
        },
        {
            id: 8,
            brand: "Vooter",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20241112/LIuo/67338e16260f9c41e8d5569e/vooter_grey_men_relaxed_fit_cargo_pants.jpg",
            name: "Men Relaxed Fit Cargo Pants",
            avgRating: 4.3,
            ratingCount: 4500,
            price: 950,
            discount: 62,
            category: 'Men'
        },
        {
            id: 9,
            brand: "RAYMOND",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20240108/5n9p/659bf96854c30e62769a8297/raymond_maroon_men_checked_slim_fit_shirt_with_patch_pocket.jpg",
            name: "Men Checked Slim Fit Shirt",
            avgRating: 3,
            ratingCount: 5,
            price: 1150,
            discount: 50,
            category: 'Men'
        },
        {
            id: 10,
            brand: "Jack & Jones",
            imageUrl:
                "https://assets.ajio.com/medias/sys_master/root/20240413/73Nl/661a2b8416fd2c6e6aafeb94/jack_%26_jones_jet_black_men_slim_fit_polo_t-shirt_.jpg",
            name: "Men Slim Fit Polo T-Shirt ",
            avgRating: 3.9,
            ratingCount: 130,
            price: 690,
            discount: 54,
            category: 'Men'
        },
        {
            id: 11,
            imageUrl: "https://assets.ajio.com/medias/sys_master/root/20250128/WVXo/67983176bc78b543a9ffdd9c/nyrika_black_women_printed_tunic.jpg",
            brand: "Nyrika",
            name: "Women Printed Tunic",
            avgRating: 3.3,
            ratingCount: 413,
            price: 1000,
            discount: 80,
            category: 'Women'
        },
        {
            id: 12,
            imageUrl: "https://assets.ajio.com/medias/sys_master/root/20250128/YV6u/679831642960820c493f3f81/nyrika_blue_women_printed_tunic.jpg",
            brand: "Leriya Fashion",
            name: "Women Printed Fit Top",
            avgRating: 4.2,
            ratingCount: 320,
            price: 1300,
            discount: 59,
            category: 'Women'
        },
        {
            id: 13,
            imageUrl: "https://assets.ajio.com/medias/sys_master/root/20241210/FLzL/67574d65c148fa1b302857bb/maheshvi_peach_women_striped_relaxed_fit_top.jpg",
            brand: "Womester",
            name: "Women Casual Top",
            avgRating: 4.1,
            ratingCount: 210,
            price: 350,
            discount: 50,
            category: 'Women'
        },
        {
            id: 14,
            imageUrl: "https://assets.ajio.com/medias/sys_master/root/20230912/HugY/64ff9689ddf7791519ce3ddf/deeps_fashions_blue_embroidered_tunic_with_flared_sleeves_.jpg",
            brand: "Lakshita",
            name: "Women Embroidered Fit Top",
            avgRating: 5.0,
            ratingCount: 12,
            price: 2186,
            discount: 27,
            category: 'Women'
        },
        {
            id: 15,
            imageUrl: "https://assets.ajio.com/medias/sys_master/root/20231025/yWqz/65392d75ddf77915195a2b03/u.s._polo_assn._black_women_embroidered_relaxed_fit_top.jpg",
            brand: "U.S. Polo Assn.",
            name: "Blouson Top with Cuffed Sleeves",
            avgRating: 3.4,
            ratingCount: 114,
            price: 3219,
            discount: 39,
            category: 'Women'
        },
        {
            id: 16,
            imageUrl: "https://assets.ajio.com/medias/sys_master/root/20241119/uIaS/673c538e0f47f80c8795433c/nishabd_off_white_women_floral_printed_pure_cotton_top.jpg",
            brand: "FabIndia",
            name: "Cotton Printed Kurta",
            avgRating: 4.5,
            ratingCount: 526,
            price: 1200,
            discount: 25,
            category: 'Women'
        },
        {
            id: 17,
            imageUrl: "https://assets.ajio.com/medias/sys_master/root/20240816/gUi6/66bf7cf76f60443f310fe59c/fiorra_black_women_relaxed_fit_floral_print_top.jpg",
            brand: "H&M",
            name: "Casual Crop Top",
            avgRating: 4.0,
            ratingCount: 350,
            price: 750,
            discount: 30,
            category: 'Women'
        },
        {
            id: 18,
            imageUrl: "https://assets.ajio.com/medias/sys_master/root/20240728/WnkR/66a5fd686f60443f31d1f372/tior_white_floral_print_square-neck_peplum_top.jpg",
            brand: "Zara",
            name: "Elegant Party Wear",
            avgRating: 4.7,
            ratingCount: 275,
            price: 2500,
            discount: 45,
            category: 'Women'
        },
        {
            id: 19,
            imageUrl: "https://assets.ajio.com/medias/sys_master/root/20241211/xqpr/6758c0ff0f47f80c87edd970/maheshvi_beige_women_animal_top.jpg",
            brand: "Forever 21",
            name: "Floral Print Dress",
            avgRating: 4.3,
            ratingCount: 198,
            price: 1800,
            discount: 40,
            category: 'Women'
        },
        {
            id: 20,
            imageUrl: "https://assets.ajio.com/medias/sys_master/root/20241114/HEOZ/6734ffda260f9c41e8df13e2/leriya_fashion_white_women_loose_fit_top.jpg",
            brand: "Levi's",
            name: "Denim Jacket",
            avgRating: 4.8,
            ratingCount: 610,
            price: 3500,
            discount: 35,
            category: 'Women'
        },
    ];
    const [filteredCloth, setFilteredCloth] = useState({});
    console.log(params.id);

    console.log(searchParams.get('name'));

    useEffect(() => {

        const filteredData = clothes.filter(cloth => cloth.id == params.id);

        setFilteredCloth(filteredData[0]);
    
        console.log(filteredData[0]);

    }, []);

    const brandStyles = {
        color: 'red',
        fontSize: '30px'
    }

    return (
        <div className="m-10">
            <h1 className="text-3xl font-semibold text-center">Cloth Details</h1>
            {filteredCloth && (
                <div className="flex">
                    <div className="w-1/3">

                        <img src={filteredCloth.imageUrl} />

                    </div>
                
                    <div className="w-2/3">
                        <h3 className="font-semibold text-2xl my-2" style={{ color: 'blue', fontSize: '40px' }}>{filteredCloth.name}</h3>
                        
                        <h3 className="font-semibold text-xl my-2" style={brandStyles}>{filteredCloth.brand}</h3>

                        <h3 className="font-semibold text-xl my-2 price">RS. {filteredCloth.price}</h3>


                    </div>
                </div>
            )}

        </div>

    )
}

export default ClothDetails;