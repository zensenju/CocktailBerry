import { useState } from 'react';
import { useConfig } from '../../ConfigProvider';
import { FaPlus, FaMinus } from 'react-icons/fa';
import { calibrateBottle } from '../../api/bottles';
import { executeAndShow } from '../../utils';

const CalibrationWindow = () => {
  const [channel, setChannel] = useState(1);
  const [amount, setAmount] = useState(10);
  const { config } = useConfig();

  return (
    <div className='flex flex-col justify-between items-center p-4 w-full max-w-md'>
      <h1 className='text-secondary text-2xl font-bold mb-8'>Pump Calibration Program</h1>
      <div className='grid grid-cols-3 gap-4 items-center w-full max-w-sm'>
        <div className='text-center'>
          <div className='text-4xl font-bold'>{channel}</div>
        </div>
        <div className='flex flex-col space-y-2'>
          <button
            className='button-primary button-primary p-2 flex justify-center items-center'
            onClick={() => setChannel(Math.min(channel + 1, config.MAKER_NUMBER_BOTTLES))}
          >
            <FaPlus size={30} />
          </button>
          <button
            className='button-primary p-2 flex justify-center items-center'
            onClick={() => setChannel(Math.max(1, channel - 1))}
          >
            <FaMinus size={30} />
          </button>
        </div>
        <div className='text-center text-lg font-semibold text-neutral'>Pump</div>

        <div className='text-center'>
          <div className='text-4xl font-bold'>{amount}</div>
        </div>
        <div className='flex flex-col space-y-2'>
          <button
            className='button-primary p-2 button-primary flex justify-center items-center'
            onClick={() => setAmount(amount + 10)}
          >
            <FaPlus size={30} />
          </button>
          <button
            className='button-primary p-2 button-primary flex justify-center items-center'
            onClick={() => setAmount(Math.max(10, amount - 10))}
          >
            <FaMinus size={30} />
          </button>
        </div>
        <div className='text-center text-lg font-semibold text-neutral'>Amount</div>
      </div>

      <button
        className='button-primary-filled text-lg p-4 w-full mt-8'
        onClick={() => executeAndShow(() => calibrateBottle(channel, amount))}
      >
        Start
      </button>
    </div>
  );
};

export default CalibrationWindow;
