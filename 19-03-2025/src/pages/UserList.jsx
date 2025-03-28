import User from '../components/User'
import axios from 'axios';
import { useState, useEffect } from 'react';

function UserList() {
    const [users, setUsers] = useState([]);
    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        try {
            const response = await axios.get('http://localhost:4000/users');

            console.log(response.data);

            setUsers(response.data);
        } catch(error) {
            console.log(error);
        }
    };

    const deleteUser = async (id) => {
        console.log(id);
        try {
            await axios.delete('http://localhost:4000/users/' + id);
            fetchUsers();
        } catch(error) {
            console.log(error);
        }
    };

    return (
        <div className='border m-2 p-4'>
            <h1 className="text-4xl text-center text-blue-500 my-4">User List</h1>

            <div className='flex gap-10 flex-wrap justify-between p-4'>
                {users.map(user => (
                    <div className='w-md'>
                        <User user={user} username={user.username} deleteUser={deleteUser}/>
                    </div>
                ))}
            </div>
        </div>
    )


}

export default UserList;