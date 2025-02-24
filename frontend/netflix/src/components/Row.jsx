import React, { useEffect, useState } from "react";
import axios from "axios";
import Movie from "./Movie";
import { MdChevronLeft, MdChevronRight } from "react-icons/md";

const Row = ({ title, movies, rowID }) => {
  /*  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);

/*   useEffect(() => {
    console.log("fetchURL:", fetchURL);
    axios
      .get(fetchURL)
      .then((response) => {
        console.log("response.data:", response.data);
        if (response.data?.results) {
          setMovies(response.data.results);
        } else {
          console.error("No results found.");
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching movies:", error);
        setLoading(false);
      });
  }, [fetchURL]); */

  const slideLeft = () => {
    var slider = document.getElementById("slider" + rowID);
    slider.scrollLeft = slider.scrollLeft - 500;
  };

  const slideRight = () => {
    var slider = document.getElementById("slider" + rowID);
    slider.scrollLeft = slider.scrollLeft + 500;
  };

  /*   if (loading) {
    return <div>Loading...</div>;
  } */

  return (
    <>
      <h2 className="text-white font-bold md:text-xl p-4"> {title} </h2>
      <div className="relative flex items-center group ">
        <MdChevronLeft
          onClick={slideLeft}
          className="bg-white left-0 rounded-full absolute opacity-50 hover:opacity-100 cursor-pointer z-10 hidden group-hover:block"
          size={40}
        />
        <div
          id={"slider" + rowID}
          className="w-full h-full overflow-x-scroll whitespace-nowrap scroll-smooth scrollbar-hide relative"
        >
          {movies?.map((item, index) => (
            <Movie key={index} item={item} />
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

export default Row;
