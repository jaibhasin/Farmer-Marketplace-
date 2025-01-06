import axios from "axios";

async function getcropdata() {
    try {
        const response = await axios.get("http://127.0.0.1:5000/farmer/list-crops/", {
            withCredentials: true, // Ensures cookies (session) are sent
        });

        console.log("Crop data fetched:", response.data);
        if (Array.isArray(response.data)) {
            return response.data;
        } else {
            throw new Error("Unexpected response format");
        }
    } catch (error) {
        console.error("Error while fetching crop data: ", error);
        if (error.response && error.response.status === 401) {
            console.log("User not authenticated, redirecting to login...");
        }
        throw new Error("Failed to fetch crop data");
    }
}

export default getcropdata;
