import { useState, useEffect } from 'react';

function Employees() {
    const [employees, setEmployees] = useState([]);
    useEffect(() => {
        fetchEmployees();
    }, []);

    const fetchEmployees = async () => {
        try {
            const response = await fetch('https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001');
            const parsedResponse = await response.json();
            setEmployees(parsedResponse);
        } catch(error) {
            console.log(error);
        }
    };

    return (
        <div>
            <h1>Employee List</h1>

            <div className='flex gap-x-10 flex-wrap gap-y-10 space-between'>
                {employees.map(employee => (
                    <div key={employee.id} className='w-100'>
                        <div className='shadow px-4 py-3'>
                            <p>Name: <span className='font-semibold text-lg'>{employee.firstName} {employee.lastName}</span></p>
                            <p>Email: <span className='font-semibold text-lg'>{employee.email}</span></p>
                            <p>Contact No: <span className='font-semibold text-lg'>{employee.contactNumber}</span></p>
                            <p>Age: <span className='font-semibold text-lg'>{employee.age}</span></p>
                            <p>DOB: <span className='font-semibold text-lg'>{employee.dob}</span></p>
                            <p>Salary: <span className='font-semibold text-lg'>{employee.salary}</span></p>
                            <p>Address: <span className='font-semibold text-lg'>{employee.address}</span></p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Employees;