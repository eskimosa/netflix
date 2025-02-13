import axios from "axios";
import React, { useEffect, useState } from "react";
import baseUrl from "./shared/baseUrl";

const Main = () => {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetching movies from the API
  useEffect(() => {
    axios
      .get(`${baseUrl}/api/movies/`)
      .then((response) => {
        setMovies(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching movies:", error);
        setLoading(false);
      });
  }, []);

  // Only select a random movie if movies array is not empty
  const movie =
    movies.length > 0
      ? movies[Math.floor(Math.random() * movies.length)]
      : null;

  const imageUrl = movie ? movie.poster_path.replace("/w500", "/original") : "";

  if (loading) {
    return <div>Loading...</div>;
  }

  const trancateString = (str, num) => {
    if (str?.length > num) {
      return str.slice(0, num) + "...";
    } else {
      return str;
    }
  };

  console.log(movie);

  return (
    <div className="w-full h-[800px] text-white">
      <div className="w-full h-full">
        <div className="absolute w-full h-[800px] bg-gradient-to-r from-black"></div>
        <img
          className="w-full h-full object-cover"
          src={imageUrl}
          alt={movie.title}
        />
        <div className="absolute w-full top-[20%] p-4 md:p-3 ">
          <h1 className="text-3xl md:text-5xl font-bold">{movie.title}</h1>
          <div className="my-4">
            <button className="border bg-gray-300 text-black border-gray-300 py-2 px-5">
              Play
            </button>
            <button className="border text-white border-gray-300 py-2 px-5 ml-4">
              Watch Later
            </button>
          </div>
          <p className="text-gray-400 text-sm">
            Released: {movie?.release_date}{" "}
          </p>
          <p className="w-full md:max-w-[70%] lg:max-w-[50%] xl:max-w-[35%] text-gray-200">
            {trancateString(movie?.description, 150)}
          </p>
        </div>
      </div>
    </div>
  );
};

export default Main;
