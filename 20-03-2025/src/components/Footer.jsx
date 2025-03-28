function Footer() {

    return (
        <footer className="bg-gray-900 text-gray-400 py-10">
            <div className="container mx-auto px-6">
                <div className="flex flex-col items-center text-center md:text-left md:flex-row md:justify-between">
                    {/* Logo and Description */}
                    <div className="mb-6 md:mb-0">
                        <div className="flex items-center space-x-2">
                            <span className="text-2xl text-indigo-400 font-bold">🌊</span>
                        </div>
                        <p className="mt-2 max-w-xs text-sm">
                            Making the world a better place through constructing elegant hierarchies.
                        </p>
                        {/* Social Icons */}
                        <div className="flex space-x-4 mt-4">
                            <a href="#" className="text-gray-500 hover:text-white"><i className="fab fa-facebook"></i></a>
                            <a href="#" className="text-gray-500 hover:text-white"><i className="fab fa-instagram"></i></a>
                            <a href="#" className="text-gray-500 hover:text-white"><i className="fab fa-x-twitter"></i></a>
                            <a href="#" className="text-gray-500 hover:text-white"><i className="fab fa-github"></i></a>
                            <a href="#" className="text-gray-500 hover:text-white"><i className="fab fa-youtube"></i></a>
                        </div>
                    </div>

                    {/* Footer Links */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
                        <div>
                            <h3 className="text-white font-semibold">Solutions</h3>
                            <ul className="mt-2 space-y-2 text-sm">
                                <li><a href="#" className="hover:text-white">Marketing</a></li>
                                <li><a href="#" className="hover:text-white">Analytics</a></li>
                                <li><a href="#" className="hover:text-white">Automation</a></li>
                                <li><a href="#" className="hover:text-white">Commerce</a></li>
                                <li><a href="#" className="hover:text-white">Insights</a></li>
                            </ul>
                        </div>
                        <div>
                            <h3 className="text-white font-semibold">Support</h3>
                            <ul className="mt-2 space-y-2 text-sm">
                                <li><a href="#" className="hover:text-white">Submit Ticket</a></li>
                                <li><a href="#" className="hover:text-white">Documentation</a></li>
                                <li><a href="#" className="hover:text-white">Guides</a></li>
                            </ul>
                        </div>
                        <div>
                            <h3 className="text-white font-semibold">Company</h3>
                            <ul className="mt-2 space-y-2 text-sm">
                                <li><a href="#" className="hover:text-white">About</a></li>
                                <li><a href="#" className="hover:text-white">Blog</a></li>
                                <li><a href="#" className="hover:text-white">Jobs</a></li>
                                <li><a href="#" className="hover:text-white">Press</a></li>
                            </ul>
                        </div>
                        <div>
                            <h3 className="text-white font-semibold">Legal</h3>
                            <ul className="mt-2 space-y-2 text-sm">
                                <li><a href="#" className="hover:text-white">Terms of Service</a></li>
                                <li><a href="#" className="hover:text-white">Privacy Policy</a></li>
                                <li><a href="#" className="hover:text-white">License</a></li>
                            </ul>
                        </div>
                    </div>
                </div>

                {/* Copyright */}
                <div className="border-t border-gray-700 mt-8 pt-6 text-center text-sm">
                    <p>© 2024 Your Company, Inc. All rights reserved.</p>
                </div>
            </div>
        </footer>
    )
}

export default Footer;