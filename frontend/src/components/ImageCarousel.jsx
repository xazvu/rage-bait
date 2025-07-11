// src/components/ImageCarousel.jsx
import React, { useState } from 'react';

export default function ImageCarousel({ images }) {
  const [currentIndex, setCurrentIndex] = useState(0);

  const nextSlide = () => {
    setCurrentIndex((prev) => (currentIndex === images.length - 1 ? 0 : prev + 1));
  };

  const prevSlide = () => {
    setCurrentIndex((prev) => (currentIndex === 0 ? images.length - 1 : prev - 1));
  };

  const currentImage = images[currentIndex];

  return (
    <div className="carousel-container">
      <button className="carousel-btn prev" onClick={prevSlide}>❮</button>
      <img src={currentImage.url} alt={`#${currentIndex}`} className="carousel-image" />
      <button className="carousel-btn next" onClick={nextSlide}>❯</button>
    </div>
  );
}