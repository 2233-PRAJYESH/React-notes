import DeleteUser from './DeleteUser';
import { useState } from 'react';

function User(props) {
    console.log(props);
    const [isVisible, setIsVisible] = useState(false);

    return (
        <div className="shadow-xl p-6">
            <div className="flex justify-end gap-5">
                <i class="fa-solid fa-pen-to-square text-blue-500 cursor-pointer"></i>
                <i class="fa-solid fa-trash text-red-500 cursor-pointer" onClick={() => setIsVisible(true)}></i>
            </div>
            <h2 className="mb-1">Name: <span className="font-medium text-blue-400">{props.user.name}</span></h2>
            <h2 className="mb-1">Username: <span className="font-medium text-blue-400">{props.user.username}</span></h2>
            <h2 className="mb-1">Email: <span className="font-medium text-blue-400">{props.user.email}</span></h2>
            <h2 className="mb-1">Mobile: <span className="font-medium text-blue-400">{props.user.mobile}</span></h2>
            <h2 className="mb-1">Address: <span className="font-medium text-blue-400">{props.user.address}</span></h2>
            <h2 className="mb-1">Role: <span className="font-medium text-blue-400">{props.user.role}</span></h2>
            <h2 className="mb-1">Status: <span className="font-medium text-blue-400">{props.user.status}</span></h2>
            <h2 className="mb-1">Created At: <span className="font-medium text-blue-400">{props.user.createdAt}</span></h2>

            {isVisible && <DeleteUser setIsVisible={setIsVisible} deleteUser={props.deleteUser} id={props.user.id}/>}
        </div>
    )
}

export default User;