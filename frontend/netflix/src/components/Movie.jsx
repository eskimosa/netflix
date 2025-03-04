import React from "react";
import { FaHeart, FaRegHeart } from "react-icons/fa";
import { useState } from "react";
import { useAuth } from "./AuthProvider";
import axios from "axios";
import baseUrl from "./shared/baseUrl";

const Movie = ({ item }) => {
  const { user } = useAuth();

  const [like, setLike] = useState(false);
  const [savedShows, setSavedShows] = useState("");
  const [saved, setSaved] = useState(false);

  const saveShow = async () => {
    if (user) {
      setLike(!like);
      setSaved(true);

      console.log("User data:", user);

      const movieData = {
        movie_id: item.tmdb_id,
      };

      // Log the data that will be sent to the backend
      console.log("Data being sent to the backend:", movieData);
      console.log(
        "Authorization Header:",
        `Bearer ${localStorage.getItem("access_token")}`
      );

      try {
        const response = await axios.post(
          `${baseUrl}/auth/user/add_movie/`,
          movieData,
          {
            headers: {
              'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
            },
          }
          
        );
        

        if (response.status === 201 || response.status === 200) {
          console.log(response.data.status); // Handle success messages here
        }
      } catch (error) {
        console.error("Error saving the movie to your list:", error);
      }
    } else {
      alert("Please log in to save movies to your list.");
    }
  };

  return (
    <div className="w-[160px] sm:w-[200px] md:w-[240px] lg:w-[280px] inline-block cursor-pointer relative p-2">
      <img
        className="w-full h-auto block"
        src={`https://image.tmdb.org/t/p/w500/${item?.poster_path}`}
        alt={item?.title}
      />
      <div className="absolute top-0 left-0 w-full h-full hover:bg-black/80 opacity-0 hover:opacity-100 text-white">
        <p className="white-space-normal text-xs md:text-sm font-bold flex justify-center items-center h-full text-center">
          {item?.title}{" "}
        </p>
        <p onClick={saveShow}>
          {like ? (
            <FaHeart className="absolute top-4 left-4 text-gray-300" />
          ) : (
            <FaRegHeart className="absolute top-4 left-4 text-gray-300" />
          )}
        </p>
      </div>
    </div>
  );
};

export default Movie;
