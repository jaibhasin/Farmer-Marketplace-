import axios from "axios";

async function getcropdata() {
    try {
        // Retrieve the token from localStorage
        const token = localStorage.getItem("jwt_token");

        if (!token) {
            console.error("No authentication token found. Please log in.");
            throw new Error("No authentication token found.");
        }

        console.log("JWT Token being sent:", token); // Log the token for debugging

        // Make the API call
        const response = await axios.get("http://127.0.0.1:5000/farmer/list-crops/", {
            headers: {
                Authorization: `Bearer ${token}`, // Ensure the format is correct
                "Content-Type": "application/json",
            },
            withCredentials: true, // Ensure cookies are sent
        });

        // Validate the response
        if (Array.isArray(response.data)) {
            console.log("Crop data fetched successfully:", response.data);
            return response.data;
        } else {
            throw new Error("Unexpected response format");
        }
    } catch (error) {
        console.error("Error fetching crop data:", error);

        if (error.response) {
            console.error("Server responded with status:", error.response.status);
            console.error("Response data:", error.response.data);

            if (error.response.status === 401) {
                console.log("User not authenticated, redirecting to login...");
                // Add redirect logic here
            } else if (error.response.status === 422) {
                console.log("Validation error occurred. Check request format or data.");
            }
        }

        throw new Error("Failed to fetch crop data");
    }
}

export default getcropdata;
