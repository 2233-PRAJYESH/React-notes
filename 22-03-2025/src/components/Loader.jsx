function Loader() {
    return (
        <div id="loader" class="fixed inset-0 flex items-center justify-center bg-black opacity-80 z-50">
            <div class="flex flex-col items-center">
                <div class="w-12 h-12 border-4 border-white border-t-transparent rounded-full animate-spin"></div>
                <p class="mt-3 text-lg text-white">Loading...</p>
            </div>
        </div>
    )
}

export default Loader;