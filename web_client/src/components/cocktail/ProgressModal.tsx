import React, { useState, useEffect } from 'react';
import Modal from 'react-modal';
import { getCocktailStatus, stopCocktail } from '../../api/cocktails';

interface ProgressModalProps {
  isOpen: boolean;
  onRequestClose: () => void;
  progress: number;
  cocktailName: string;
  triggerOnClose?: () => void;
}

const ProgressModal: React.FC<ProgressModalProps> = ({
  isOpen,
  onRequestClose,
  progress,
  cocktailName,
  triggerOnClose,
}) => {
  const [currentProgress, setCurrentProgress] = useState(progress);
  const [currentStatus, setCurrentStatus] = useState<string>('IN_PROGRESS');
  const [message, setMessage] = useState<string | null>(null);

  const closeWindow = () => {
    setCurrentProgress(0);
    setMessage(null);
    onRequestClose();
    if (triggerOnClose) {
      triggerOnClose();
    }
  };

  useEffect(() => {
    let intervalId: ReturnType<typeof setInterval> | null = null;

    const cancelInterval = () => {
      if (intervalId) {
        clearInterval(intervalId);
        intervalId = null;
      }
    };

    if (isOpen && !intervalId) {
      intervalId = setInterval(async () => {
        const cocktailStatus = await getCocktailStatus();
        setCurrentStatus(cocktailStatus.status);
        setCurrentProgress(cocktailStatus.progress);
        if (cocktailStatus.status === 'IN_PROGRESS') {
          return;
        }
        cancelInterval();
        if (cocktailStatus.message) {
          const formattedMessage = cocktailStatus.message.replace(/\n/g, '<br />');
          setMessage(formattedMessage);
        } else {
          closeWindow();
        }
      }, 250);
    }

    return () => {
      cancelInterval();
      console.log('cleanup');
    };
  }, [isOpen]);

  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={onRequestClose}
      contentLabel='Progress Modal'
      className='modal'
      overlayClassName='overlay z-30'
      shouldCloseOnOverlayClick={false}
    >
      <div className='progress-modal h-full flex flex-col justify-between'>
        <h2 className='text-4xl font-bold mb-8 text-center text-secondary'>{cocktailName}</h2>
        {message ? (
          <div className='text-neutral text-center' dangerouslySetInnerHTML={{ __html: message }} />
        ) : (
          <div className='w-full border-2 border-neutral overflow-hidden rounded-full'>
            <div className='bg-primary min-h-[4rem]' style={{ width: `${currentProgress}%` }}></div>
          </div>
        )}
        <div className='text-center mt-8'>
          {currentStatus === 'IN_PROGRESS' ? (
            <button className='mt-4 px-4 py-2 button-primary w-1/2' onClick={stopCocktail}>
              Cancel
            </button>
          ) : (
            <button className='mt-4 px-4 py-2 button-primary w-1/2' onClick={closeWindow}>
              Close
            </button>
          )}
        </div>
      </div>
    </Modal>
  );
};

export default ProgressModal;
