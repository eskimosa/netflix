import React, { useState, useEffect, use } from "react";
import { MdChevronLeft, MdChevronRight } from "react-icons/md";
import { useAuth } from "./AuthProvider";
import axios from "axios";
import baseUrl from "./shared/baseUrl";
import { AiOutlineClose } from "react-icons/ai";
import api from "./axiosConfig";

const SavedShows = () => {
  const { user } = useAuth();

  const [movies, setMovies] = useState([]);

  const slideLeft = () => {
    var slider = document.getElementById("slider");
    slider.scrollLeft = slider.scrollLeft - 500;
  };

  const slideRight = () => {
    var slider = document.getElementById("slider");
    slider.scrollLeft = slider.scrollLeft + 500;
  };

  useEffect(() => {
    const fetchMovies = async () => {
      if (user) {
        console.log(
          "Authorization Header:",
          `Bearer ${localStorage.getItem("access_token")}`
        );
        try {
          const response = await axios.get(
            `${baseUrl}/auth/user/list_movies/`,
            {
              headers: {
                Authorization: `Bearer ${localStorage.getItem("access_token")}`,
              },
            }
          );

          if (response.status === 201 || response.status === 200) {
            console.log(response.data.status);
            setMovies(response.data);
          }
        } catch (error) {
          console.error("Error saving the movie to your list:", error);
        }
      } else {
        alert("Please log in to save movies to your list.");
      }
    };
    fetchMovies();
  }, [user]);

  const deleteShow = async (movie_id) => {
    console.log("Movie id: ", movie_id);
    console.log(
      "Authorization Header from delete functionality:",
      `Bearer ${localStorage.getItem("access_token")}`
    );

    try {
      const response = await api.delete("/auth/user/remove_movie/", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        },
        data: { movie_id },
      });

      if (response.status === 204) {
        console.log("Movie removed successfully");
        setMovies(movies.filter((movie) => movie.movie_id !== movie_id));
      }
    } catch (error) {
      console.error("Error removing the movie to your list:", error);
    }
  };

  return (
    <>
      <h2 className="text-white font-bold md:text-xl p-4">My Shows</h2>
      <div className="relative flex items-center group ">
        <MdChevronLeft
          onClick={slideLeft}
          className="bg-white left-0 rounded-full absolute opacity-50 hover:opacity-100 cursor-pointer z-10 hidden group-hover:block"
          size={40}
        />
        <div
          id={"slider"}
          className="w-full h-full overflow-x-scroll whitespace-nowrap scroll-smooth scrollbar-hide relative"
        >
          {movies.map((item, index) => (
            <div
              key={index}
              className="w-[160px] sm:w-[200px] md:w-[240px] lg:w-[280px] inline-block cursor-pointer relative p-2"
            >
              <img
                className="w-full h-auto block"
                src={`https://image.tmdb.org/t/p/w500/${item?.poster_path}`}
                alt={item?.title}
              />
              <div className="absolute top-0 left-0 w-full h-full hover:bg-black/80 opacity-0 hover:opacity-100 text-white">
                <p className="white-space-normal text-xs md:text-sm font-bold flex justify-center items-center h-full text-center">
                  {item?.title}
                </p>
                <p
                  onClick={() => deleteShow(item.movie_id)}
                  className="absolute text-gray-300 top-4 right-4"
                >
                  <AiOutlineClose />
                </p>
              </div>
            </div>
          ))}
        </div>
        <MdChevronRight
          onClick={slideRight}
          className="bg-white right-0 rounded-full absolute opacity-50 hover:opacity-100 cursor-pointer z-10 hidden group-hover:block"
          size={40}
        />
      </div>
    </>
  );
};

export default SavedShows;
