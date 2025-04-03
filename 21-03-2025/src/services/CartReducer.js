function reducer(state, action) {
    console.log(action);

    switch(action.type) {
        case 'REMOVE': {
            const filteredClothes = state.filter(cloth => cloth.id !== action.id);

            return filteredClothes;
        } 
        case 'INCREMENT': {

            const modifiedClothes = state.map(cloth => {
                if (cloth.id === action.id) {
                    return { ...cloth, quantity: cloth.quantity + 1 };
                } else {
                    return cloth;
                }
            });
            return modifiedClothes;
        }
        case 'DECREMENT': {
            const modifiedClothes = state.map(cloth => {
                if (cloth.id === action.id) {
                    return { ...cloth, quantity: cloth.quantity - 1 };
                } else {
                    return cloth;
                }
            });
            return modifiedClothes;
        }
        case 'ADD': {
            return action.data;
        }
    }

    return state;
}

export default reducer;