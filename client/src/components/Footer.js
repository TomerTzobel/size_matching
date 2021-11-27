import React from 'react'

export const Footer = () => {
    return (
<footer className="page-footer font-small blue pt-4 bg-dark text-white mt-5">
    <div className="container-fluid text-center text-md-left">
        <div className="row">
            <div className="col-md-6 mt-md-0 mt-3">
            <h5 className="text-uppercase"> find your perfect size </h5>
            <p className> Using modern machine-learning algorithms, <br></br> 
            We provide personalized size recommendations </p> 
            <p className="text-secondary"> Your private information is not shared </p>
                </div>

            <hr className="clearfix w-100 d-md-none pb-0"/>

            <div className="col-md-3 mb-md-0 mb-3">
                <h5 className="text-uppercase">Website</h5>
                <ul className="list-unstyled">
                <li><a href="#!">About us</a></li>
                    <li><a href="#!">Contact</a></li>
                    <li><a href="#!">Services</a></li>
                    <li><a href="#!">Privacy</a></li>

                </ul>
            </div>

            <div className="col-md-3 mb-md-0 mb-3">
                <h5 className="text-uppercase">Social Media</h5>
                <ul className="list-unstyled">
                <li><a href="#!">Facebook</a></li>
                    <li><a href="#!">Instagram</a></li>
                    <li><a href="#!">Twitter</a></li>
                    <li><a href="#!">TikTok</a></li>

                </ul>
            </div>
        </div>
    </div>
    <div className="footer-copyright text-center py-3">© 2020 Copyright: {" "} 
        <a href="#!">SizeMatcher.com</a>
    </div>



</footer>
    )
}
