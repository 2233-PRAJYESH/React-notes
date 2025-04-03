import { useForm } from 'react-hook-form';
import { useContext } from 'react';
import EmployeeContext from '../services/EmployeeContext';
import axios from 'axios';

function AddEmployee() {
    const { register, handleSubmit } = useForm();
    const { setIsAddEmpVisible, fetchEmployees } = useContext(EmployeeContext);

    const addEmployee = async (formValues) => {
        try {
            const response = await axios.post('http://localhost:4000/employees', formValues);
            fetchEmployees();
            setIsAddEmpVisible(false);
        } catch(error) {

        }
    };

    return (
        <div className="fixed inset-0 flex items-center justify-center bg-[rgba(0,0,0,0.3)] z-50">
            <div className="bg-white p-6 rounded-lg shadow-lg w-96 animate-fadeIn">
                <h2 className="text-lg font-semibold text-gray-900">Add Employee</h2>

                <form onSubmit={handleSubmit(addEmployee)} noValidate>
                    <div>
                        <label for="firstname" className="block text-sm/6 font-medium text-gray-900">Firstname</label>
                        <div className="mt-2">
                            <input type="text" {...register('firstname')} name="firstname" id="firstname" className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" />
                        </div>
                    </div>
                    <div>
                        <label for="lastname" className="block text-sm/6 font-medium text-gray-900">Lastname</label>
                        <div className="mt-2">
                            <input type="text" {...register('lastname')} name="lastname" id="lastname" className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" />
                        </div>
                    </div>

                    <div>
                        <label for="phoneno" className="block text-sm/6 font-medium text-gray-900">Phone No</label>
                        <div className="mt-2">
                            <input type="text" {...register('phoneno')} name="phoneno" id="phoneno" className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" />
                        </div>
                    </div>

                    <div>
                        <label for="email" className="block text-sm/6 font-medium text-gray-900">Email</label>
                        <div className="mt-2">
                            <input type="email" {...register('email')} name="email" id="email" className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" />
                        </div>
                    </div>

                    <div className="mb-2">
                        <label for="role" className="block text-sm/6 font-medium text-gray-900">Role</label>
                        <div className="mt-2">
                            <select {...register('role')} className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6">
                                <option value="">Select Role</option>
                                <option>Admin</option>
                                <option>Employee</option>
                            </select>
                        </div>
                    </div>

                    <div className='flex gap-x-10 my-2'>
                        <button type="button" onClick={() => setIsAddEmpVisible(false)} className="flex w-full justify-center rounded-md bg-red-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Cancel</button>
                        <button type="submit" className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
                    </div>
                </form>
            </div>
        </div>
    )

}

export default AddEmployee;