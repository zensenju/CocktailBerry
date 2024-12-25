import React, { useState } from 'react';
import Modal from 'react-modal';
import { useCocktails } from '../../api/cocktails';
import { Cocktail } from '../../types/models';
import CocktailSelection from './CocktailSelection';
import { MdNoDrinks } from 'react-icons/md';
import { API_URL } from '../../api/common';
import ErrorComponent from '../common/ErrorComponent';
import LoadingData from '../common/LoadingData';
import { useConfig } from '../../ConfigProvider';
import SingleIngredientSelection from './SingleIngredientSelection';
import { FaEraser, FaSearch } from 'react-icons/fa';

Modal.setAppElement('#root');

const CocktailList: React.FC = () => {
  const { data: cocktails, error, isLoading } = useCocktails();
  const [selectedCocktail, setSelectedCocktail] = useState<Cocktail | null>(null);
  const [singleIngredientOpen, setSingleIngredientOpen] = useState(false);
  const [showSearch, setShowSearch] = useState(false);
  const [search, setSearch] = useState('');
  const { config } = useConfig();

  if (isLoading) return <LoadingData />;
  if (error) return <ErrorComponent text={error.message} />;

  const handleCocktailClick = (cocktail: Cocktail) => {
    setSelectedCocktail(cocktail);
  };

  const handleCloseModal = () => {
    setSelectedCocktail(null);
  };

  let displayedCocktails = cocktails;

  if (showSearch && search) {
    displayedCocktails = displayedCocktails?.filter(
      (cocktail) =>
        cocktail.name.toLowerCase().includes(search.toLowerCase()) ||
        cocktail.ingredients.some((ingredient) => ingredient.name.toLowerCase().includes(search.toLowerCase())),
    );
  }

  return (
    <div className='px-2 centered max-w-7xl'>
      <div className='sticky-top mb-2 flex flex-row'>
        <div className='flex-grow'></div>
        <input
          type='text'
          placeholder='Search'
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className='input-base mr-1 w-full p-3 max-w-sm'
          hidden={!showSearch}
        />
        <div hidden={!showSearch}>
          <button
            onClick={() => setSearch('')}
            className='button-neutral flex items-center justify-center p-2 mr-1 !border'
          >
            <FaEraser size={20} />
          </button>
        </div>
        <button
          onClick={() => setShowSearch(!showSearch)}
          className='button-primary flex items-center justify-center p-2 !border pointer-events-auto'
        >
          <FaSearch size={20} />
        </button>
      </div>
      <div className='flex flex-wrap gap-3 justify-center items-center w-full'>
        {displayedCocktails
          ?.sort((a, b) => a.name.localeCompare(b.name))
          .map((cocktail) => (
            <div
              key={cocktail.id}
              className='border-2 border-primary hover:border-secondary rounded-xl box-border overflow-hidden min-w-56 max-w-64 basis-1 grow text-xl font-bold bg-primary hover:bg-secondary text-background'
              onClick={() => handleCocktailClick(cocktail)}
            >
              <h2 className='text-center py-1 flex items-center justify-center'>
                {cocktail.virgin_available && <MdNoDrinks className='mr-2' />}
                {cocktail.name}
              </h2>
              <div className='relative w-full' style={{ paddingTop: '100%' }}>
                <img
                  src={`${API_URL}${cocktail.image}`}
                  alt={cocktail.name}
                  className='absolute top-0 left-0 w-full h-full object-cover'
                />
              </div>
            </div>
          ))}
        {config.MAKER_ADD_SINGLE_INGREDIENT && (
          <div
            className='border-2 border-primary hover:border-secondary rounded-xl box-border overflow-hidden min-w-56 max-w-64 basis-1 grow text-xl font-bold bg-primary hover:bg-secondary text-background'
            onClick={() => setSingleIngredientOpen(true)}
          >
            <h2 className='text-center py-1 flex items-center justify-center'>Single Ingredient</h2>
            <div className='relative w-full' style={{ paddingTop: '100%' }}>
              <img
                src={`${API_URL}/static/default/default.jpg`}
                alt='Single Ingredient'
                className='absolute top-0 left-0 w-full h-full object-cover'
              />
            </div>
          </div>
        )}
      </div>

      {selectedCocktail && (
        <Modal
          isOpen={!!selectedCocktail}
          onRequestClose={handleCloseModal}
          contentLabel='Cocktail Details'
          className='modal'
          overlayClassName='overlay z-20'
        >
          <CocktailSelection selectedCocktail={selectedCocktail} handleCloseModal={handleCloseModal} />
        </Modal>
      )}
      <Modal isOpen={singleIngredientOpen} className='modal slim' overlayClassName='overlay z-20'>
        <SingleIngredientSelection onClose={() => setSingleIngredientOpen(false)} />
      </Modal>
    </div>
  );
};

export default CocktailList;
