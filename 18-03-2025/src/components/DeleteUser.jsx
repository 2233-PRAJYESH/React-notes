function DeleteUser(props) {

    return (
        <div className="fixed inset-0 flex items-center justify-center bg-[rgba(0,0,0,0.3)] z-50">
            <div className="bg-white p-6 rounded-lg shadow-lg w-96 animate-fadeIn">
                <h2 className="text-lg font-semibold text-gray-900">Delete User</h2>
                <p className="mt-2 text-gray-600">Are you sure you want to delete this user? This action cannot be undone.</p>

                <div className="mt-4 flex justify-end space-x-2">
                    <button
                        className="px-4 py-2 bg-gray-200 text-gray-800 rounded hover:bg-gray-300 transition"
                        onClick={() => props.setIsVisible(false)}
                    >
                        Cancel
                    </button>
                    <button
                        className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 transition"
                        onClick={() => { props.deleteUser(props.id); props.setIsVisible(false); }}
                    >
                        Delete
                    </button>
                </div>
            </div>
        </div>

    )

}

export default DeleteUser;