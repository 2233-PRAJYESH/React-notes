import { useState, useEffect } from 'react';
import AddEmployee from './AddEmployee';
import EmployeeContext from '../services/EmployeeContext';
import Loader from '../components/Loader';

function Employees() {
    const [employees, setEmployees] = useState([]);
    const [isAddEmpVisible, setIsAddEmpVisible] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    useEffect(() => {
        fetchEmployees();
    }, []);

    const fetchEmployees = async () => {
        try {
            setIsLoading(true);
            const response = await fetch('http://localhost:4000/employees');
            setTimeout(() => {
                setIsLoading(false);
            }, 500);
            const parsedResponse = await response.json();
            setEmployees(parsedResponse);
        } catch(error) {
            console.log(error);
        }
    };

    return (
        <div>
            <h1 className='text-center text-3xl my-4 text-blue-400'>Employee List</h1>
            

            <div className='flex justify-end mx-20 mb-2'>
                <button className='rounded bg-blue-400 text-white px-2 py-1 cursor-pointer' onClick={() => setIsAddEmpVisible(true)}>+ Add Employee</button>
            </div>

            <EmployeeContext value={{ setIsAddEmpVisible: setIsAddEmpVisible, fetchEmployees: fetchEmployees }}>
                {isLoading ? (<Loader/>) : (
                    <div className='flex gap-x-10 flex-wrap gap-y-10 space-between mx-15 mb-5'>
                        {employees.map(employee => (
                            <div key={employee.id} className='w-100'>
                                <div className='shadow px-4 py-3'>
                                    <p>Name: <span className='font-semibold text-lg'>{employee.firstname} {employee.lastname}</span></p>
                                    <p>Email: <span className='font-semibold text-lg'>{employee.email}</span></p>
                                    <p>Phone No: <span className='font-semibold text-lg'>{employee.phoneno}</span></p>
                                    <p>Role: <span className='font-semibold text-lg'>{employee.role}</span></p>
                                </div>
                            </div>
                        ))}
                    </div>
                )}

                {isAddEmpVisible && <AddEmployee/>}

            </EmployeeContext>

        </div>
    )
}

export default Employees;