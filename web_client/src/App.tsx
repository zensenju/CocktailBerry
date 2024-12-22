import CocktailList from './components/cocktail/CocktailList.tsx';
import { Route, Routes, Navigate, BrowserRouter } from 'react-router-dom';
import Header from './components/Header.tsx';
import { useConfig } from './ConfigProvider.tsx';
import IngredientList from './components/ingredient/IngredientList.tsx';
import RecipeList from './components/recipe/RecipeList.tsx';
import BottleList from './components/bottle/BottleList.tsx';
import AvailableBottles from './components/bottle/AvailableBottles.tsx';
import OptionWindow from './components/options/OptionWindow.tsx';
import CalibrationWindow from './components/options/CalibrationWindow.tsx';
import ConfigWindow from './components/options/ConfigWindow.tsx';
import DataWindow from './components/options/DataWindow.tsx';
import LogWindow from './components/options/LogWindow.tsx';
import WifiManager from './components/options/WifiManager.tsx';
import { ToastContainer } from 'react-toastify';
import GettingConfiguration from './components/common/GettingConfiguration.tsx';
import AddonManager from './components/options/AddonManager.tsx';

function App() {
  const { theme, config } = useConfig();

  return (
    <div className={`${theme} min-h-screen`}>
      <BrowserRouter>
        <Header />
        <div className='app-container pt-12'>
          <ToastContainer position='top-center' />
          {/* do not show routes when config is empty */}
          {Object.keys(config).length === 0 ? (
            <GettingConfiguration />
          ) : (
            <Routes>
              <Route path='cocktails' element={<CocktailList />} />
              <Route path='ingredients' element={<IngredientList />} />
              <Route path='recipes' element={<RecipeList />} />
              <Route path='bottles' element={<BottleList />} />
              <Route path='bottles/available' element={<AvailableBottles />} />
              <Route path='options' element={<OptionWindow />} />
              <Route path='configuration' element={<ConfigWindow />} />
              <Route path='data' element={<DataWindow />} />
              <Route path='logs' element={<LogWindow />} />
              <Route path='wifi' element={<WifiManager />} />
              <Route path='addons' element={<AddonManager />} />
              <Route path='calibration' element={<CalibrationWindow />} />
              <Route path='/' element={<Navigate to='/cocktails' />} />
            </Routes>
          )}
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
