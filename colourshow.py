   ��n�6�^�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        lower_colourrange = np.array([64,100,100])
    upper_colourrange = np.array([84,255,255])

    # Set the threshold of the video to output specified colour range
    mask = cv2.inRange(colour, lower_colourrange, upper_colourrange)

    # Use Bitwise-AND command to set mask and the original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #display the 3 windows (frame, mask, res) and wait for esc key or ctrl+c to end program
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    end = cv2.waitKey(5) & 0xFF
    if end == 27:
        break

#close all windows opened by program
cv2.destroyAllWindows()
