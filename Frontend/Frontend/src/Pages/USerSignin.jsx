import { useRecoilValue } from "recoil";
import { languageatom } from "../atoms/languageatom";
import { useState } from "react";
import axios from "axios"
import { useNavigate } from "react-router-dom";

export default function User_Signin() {

  const navigate=useNavigate();

  const language = useRecoilValue(languageatom);

  const [userinputs, setUserInputs] = useState({
    phone: "",
    password: "",
  });

  async function handlesubmit(e) {
    e.preventDefault();
    

    try{
      const senddata=await axios.post("http://localhost:3000/user/signin",userinputs)
      // console.log(senddata.data);
      
      if((senddata.data.success)){
          alert("WELCOME")
          console.log(senddata.data);
          navigate("/user/userhome")
      }
      else{
          alert("InValid Inputs")
          console.log(senddata.data.error);
          
      }

  }catch (err){
      alert("some error occured")
      console.log(err);            
  }
    
  }
  // console.log("In Signin");
  
  function handleonchange(e) {
    const { name, value } = e.target;
    setUserInputs((prev) => ({
      ...prev,
      [name]: value,
    }));
  }

  

  return (
    <div className="w-full h-screen bg-[url('../usersigin.jp')] bg-center bg-cover  flex flex-col justify-center object-contain items-center ">
      <div className="bg-white bg-opacity-60 max-w-lg w-full sm:w-2/3 p-4 rounded-xl shadow-2xl">
        <div className="mt-4">
          <div className="flex justify-center">
            <p className="font-bold text-4xl text-[#00b4d8]">
              {language ? "Sign In" : "साइन इन"}
            </p>
          </div>
          <div className="text-center text-sm mt-2 text-gray-500">
            <p className="text-[#00b4d8]">
              {language
                ? "Enter your credentials to access your account"
                : "अपने खाते तक पहुँचने के लिए अपनी साख दर्ज करें"}
            </p>
          </div>
          <br />
        </div>
        <div className="mt-2">
          <form onSubmit={handlesubmit}>
            <label
              htmlFor="phone"
              className="font-bold text-lg text-[#00b4d8]"
            >
              {language ? "Phone No." : "फोन नंबर"}
            </label>
            <input
              type="number"
              id="phone"
              placeholder={language ? "Enter Your Phone No." : "आपका फोन नंबर"}
              name="phone"
              value={userinputs.phone}
              onChange={handleonchange}
              maxLength={10}
              className="border-2 px-3 py-1 border-[#00b4d8] w-full rounded-lg my-2 focus:border-[#0077b6]"
            />
            <br />
            <label
              htmlFor="password"
              className="font-bold text-lg text-[#00b4d8]"
            >
              {language ? "Password" : "आपका पासवर्ड"}
            </label>
            <br />
            <input
              type="password"
              id="password"
              placeholder={language ? "Password" : "आपका पासवर्ड"}
              name="password"
              value={userinputs.password}
              onChange={handleonchange}
              className="border-2 px-3 py-1 border-[#00b4d8] w-full rounded-lg my-2"
            />
            <br />
            <div className="flex justify-center my-2">
              <button
                type="submit"
                className="w-full text-white bg-[#00b4d8] hover:bg-[#0077b6] py-2 rounded-lg"
              >
                {language ? "Sign In" : "साइन इन"}
              </button>
            </div>
            <div className="flex justify-center gap-2 font-semibold pt-1 text-[#00b4d8]">
              {language
                ? "Don't have an account?"
                : "क्या आपका खाता नहीं है?"}{" "}
              <a href="http://localhost:5174/user/signup">
                <u>{language ? "Sign Up" : "साइन अप"}</u>
              </a>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
