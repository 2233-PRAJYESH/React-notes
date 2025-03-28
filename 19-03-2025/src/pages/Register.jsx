import { useForm } from 'react-hook-form';

function Register() {
    const { register, handleSubmit, formState: { errors }, watch } = useForm();

    const registerUser = (formValues) => {
        console.log(formValues);
    };

    return (
        <div className="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
            <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                <img className="mx-auto h-10 w-auto" src="https://www.digitaledify.ai/images/digitaledify-devops-python-digital-marketing-training-hyderabad.webp" alt="Your Company" />
                <h2 className="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">Sign up to your account</h2>
            </div>

            <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                <form className="space-y-3" onSubmit={handleSubmit(registerUser)} noValidate>

                    <div>
                        <label for="fullName" className="block text-sm/6 font-medium text-gray-900">Full Name</label>
                        <div className="mt-2">
                            <input {...register('fullName', { required: { value: true, message: 'Full name is required'}})} type="text" name="fullName" id="fullName" className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" />
                            <p className='text-red-500 text-sm'>{errors?.fullName?.message}</p>
                        </div>
                    </div>
                    <div>
                        <label for="email" className="block text-sm/6 font-medium text-gray-900">Email address</label>
                        <div className="mt-2">
                            <input {...register('email', { required: { value: true, message: 'Email is required'}, pattern: { value: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/, message: 'Incorrect email format'}})} type="email" name="email" id="email" className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" />
                            <p className='text-red-500 text-sm'>{errors?.email?.message}</p>
                        </div>
                    </div>

                    <div>
                        <label for="mobile" className="block text-sm/6 font-medium text-gray-900">Mobile</label>
                        <div className="mt-2">
                            <input {...register('mobile', { required: { value: true, message: 'Mobile is required'}, pattern: { value: /^[6-9]\d{9}$/, message: 'Incorrect mobile format'}})} type="text" name="mobile" id="mobile" className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" />
                            <p className='text-red-500 text-sm'>{errors?.mobile?.message}</p>
                        </div>
                    </div>

                    <div>
                        <div className="flex items-center justify-between">
                            <label for="password" className="block text-sm/6 font-medium text-gray-900">Password</label>
                            <div className="text-sm">
                                <a href="#" className="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
                            </div>
                        </div>
                        <div className="mt-2">
                            <input {...register('password', { required: { value: true, message: 'Password is required'}, pattern: { value: /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/, message: 'Incorrect password format'}})} type="password" name="password" id="password" autocomplete="current-password" className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6" />
                            <p className='text-red-500 text-sm'>{errors?.password?.message}</p>
                        </div>
                    </div>

                    <div>
                        <label for="role" className="block text-sm/6 font-medium text-gray-900">Role</label>
                        <div className="mt-2">
                            <select {...register('role')} className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6">
                                <option value="">Select Role</option>
                                <option>Admin</option>
                                <option>User</option>
                            </select>
                        </div>
                    </div>

                    <div>
                        <button type="submit" className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign up</button>
                    </div>
                </form>

                <p className="mt-10 text-center text-sm/6 text-gray-500">
                    Not a member?
                    <a href="#" className="font-semibold text-indigo-600 hover:text-indigo-500">Start a 14 day free trial</a>
                </p>
            </div>
        </div>
    )
}

export default Register;