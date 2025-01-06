import React, { useState } from 'react';
import { useSetRecoilState, useRecoilValue } from 'recoil';
import { showaddcropmodule } from "../atoms/showaddcropmodule";
import { dataadded } from "../atoms/dataadded";
import { languageatom } from '../atoms/languageatom';
import axios from 'axios';

export default function Addcropmodule() {
    const curdate = new Date();
    const fullDate = curdate.toLocaleDateString();
    const closemodule = useSetRecoilState(showaddcropmodule);
    const setdataadded = useSetRecoilState(dataadded);
    const language = useRecoilValue(languageatom);

    const [cropdata, setcropdata] = useState({
        crop: "",
        quantity: null,
        date: fullDate,
        price: null
    });

    function handleonchange(e) {
        const { name, value } = e.target;
        setcropdata(prevdata => ({
            ...prevdata,
            [name]: value
        }));
    }

    async function handleonSubmit(e) {
        e.preventDefault();

        const jwtToken = localStorage.getItem("jwt-token");
        console.log("JWT Token:", jwtToken);

        if (!jwtToken) {
            alert(!language ? "प्रमाणीकरण विफल" : "Authentication Failed");
            return;
        }

        if (!cropdata.crop || !cropdata.quantity || !cropdata.price) {
            alert(!language ? "सभी फ़ील्ड भरें" : "Fill All Fields");
            return;
        }

        const payload = {
            crop: cropdata.crop,
            quantity: Number(cropdata.quantity),
            date: cropdata.date,
            price: Number(cropdata.price)
        };

        console.log("Payload being sent:", payload);

        try {
            const response = await axios.post(
                "http://127.0.0.1:5000/farmer/add-crop/",
                payload,
                {
                    headers: {
                        Authorization: `Bearer ${jwtToken}`,
                        "Content-Type": "application/json"
                    }
                }
            );

            console.log("Server Response:", response.data);

            if (response.status === 201) {
                alert(!language ? "फसलों को सफलतापूर्वक जोड़ा गया" : "Crops Added Successfully");
                setdataadded(c => !c);
                closemodule(c => !c);
            } else {
                alert(!language ? "सर्वर त्रुटि" : "Server Error");
            }
        } catch (error) {
            console.error("Error:", error);
            alert(!language ? "फसल डेटा पोस्ट करने में त्रुटि हुई" : "Error occurred in posting crop data");
        }
    }

    function handleclosebuttonclick() {
        closemodule(c => !c);
    }

    return (
        <div
            className="fixed inset-0 flex justify-center items-center z-50 bg-black bg-opacity-70"
            style={{ minHeight: 'calc(100vh - 80px)' }}
        >
            <div className="w-full max-w-md bg-white p-8 rounded-lg shadow-lg">
                <div className="text-center mb-6">
                    <h1 className="text-2xl font-bold">{!language ? "फसल जोड़ें" : "ADD CROP"}</h1>
                    <p className="text-lg">{!language ? "विवरण दर्ज करें" : "ENTER DETAILS"}</p>
                </div>
                <form onSubmit={handleonSubmit}>
                    <div className="mb-4">
                        <label htmlFor="crop" className="block text-sm font-semibold mb-2">{language ? "फसल" : "CROP"}</label>
                        <select
                            id="crop"
                            className="w-full p-2 border rounded"
                            name='crop'
                            value={cropdata.crop}
                            onChange={handleonchange}
                        >
                            <option value="">{!language ? "फसल चुनें" : "Select a crop"}</option>
                            <option value="Wheat">{!language ? "गेहूं" : "Wheat"}</option>
                            <option value="Rice">{!language ? "चावल" : "Rice"}</option>
                        </select>
                    </div>
                    <div className="mb-4">
                        <label htmlFor="quantity" className="block text-sm font-semibold mb-2">{!language ? "मात्रा (क्विंटल)" : "Quantity (Quintal)"}</label>
                        <input
                            type="number"
                            placeholder={!language ? "मात्रा (क्विंटल)" : "Quantity (Quintal)"}
                            id="quantity"
                            className="w-full p-2 border rounded"
                            name='quantity'
                            value={cropdata.quantity || ''}
                            onChange={handleonchange}
                        />
                    </div>
                    <div className="mb-6">
                        <label htmlFor="price" className="block text-sm font-semibold mb-2">{!language ? "कीमत प्रति क्विंटल" : "Price per Quintal"}</label>
                        <input
                            type="number"
                            placeholder={!language ? "कीमत / क्विंटल" : "Price / Quintal"}
                            id="price"
                            className="w-full p-2 border rounded"
                            name='price'
                            value={cropdata.price || ''}
                            onChange={handleonchange}
                        />
                    </div>
                    <div>
                        <button
                            type="submit"
                            className="w-full p-3 bg-green-600 text-white rounded shadow"
                        >
                            {!language ? "सबमिट करें" : "SUBMIT"}
                        </button>
                    </div>
                </form>
                <div className="mt-4">
                    <button
                        className="w-full p-3 bg-gray-500 text-white rounded shadow"
                        onClick={handleclosebuttonclick}
                    >
                        {!language ? "रद्द करें" : "CANCEL"}
                    </button>
                </div>
            </div>
        </div>
    );
}
