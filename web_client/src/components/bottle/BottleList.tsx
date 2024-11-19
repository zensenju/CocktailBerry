import React, { useEffect, useState } from 'react';
import { useBottles } from '../../api/bottles';
import { useIngredients } from '../../api/ingredients';
import BottleComponent from './BottleComponent';
import { FaGear } from 'react-icons/fa6';
import { Ingredient } from '../../types/models';

const BottleList: React.FC = () => {
  const { data: bottles, error: bottlesError, isLoading: bottlesLoading } = useBottles();
  const { data: ingredients, error: ingredientsError, isLoading: ingredientsLoading } = useIngredients(false);
  const [freeIngredients, setFreeIngredients] = useState<Ingredient[]>([]);

  useEffect(() => {
    if (bottles && ingredients) {
      const bottleIngredients = bottles.map((bottle) => bottle.ingredient?.id);
      const missingIngredients = ingredients.filter((ingredient) => !bottleIngredients.includes(ingredient.id));
      setFreeIngredients(missingIngredients);
    }
  }, [bottles, ingredients]);

  if (bottlesLoading || ingredientsLoading) {
    return <div>Loading...</div>;
  }

  if (bottlesError || ingredientsError) {
    return <div>Error: {bottlesError?.message || ingredientsError?.message}</div>;
  }

  return (
    <div className='grid grid-cols-5 gap-2 p-4 w-full max-w-7xl' style={{ gridTemplateColumns: '2fr 3fr 6fr 4fr 1fr' }}>
      {bottles?.map((bottle) => (
        <BottleComponent
          key={bottle.number}
          bottle={bottle}
          freeIngredients={freeIngredients}
          setFreeIngredients={setFreeIngredients}
        />
      ))}
      <button className='border-2 rounded-md border-primary text-primary col-span-2 p-2'>Apply</button>
      <button className='border-2 rounded-md border-primary text-primary p-2'>Change</button>
      <button className='border-2 rounded-md border-primary text-primary p-2'>Available</button>
      <button className='border-2 rounded-md border-primary text-primary flex justify-center items-center max-w-12 p-2'>
        <FaGear />
      </button>
    </div>
  );
};

export default BottleList;