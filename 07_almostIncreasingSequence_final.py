def almostIncreasingSequence(sequence):
    # print("sequence: " + str(sequence))
    ciclo = 1
    count = 0
    if len(sequence) < 3:
        return True
    else:
        while ciclo < 4:
            # print("\n***********")
            # print("CICLO " + str(ciclo))
            # print("***********\n")
            for x in range(0,len(sequence)):
                # print(x)
                # print(sequence)
                if x == 0:
                    # print("x = 0")
                    if int(sequence[x]) < int(sequence[x+1]):
                        pass
                    else:
                        count = count + 1
                        # print ("count = " + str(count))
                        del sequence[x]
                        ciclo += ciclo
                        break

                if x > 0 and x < (len(sequence)-1):
                    # print("segundo if")
                    if int(sequence[x-1]) < int(sequence[x]):
                        if int(sequence[x]) < int(sequence[x+1]):
                            if int(sequence[x+1]) <= int(sequence[x-1]):
                                del sequence[x+1]
                                ciclo += ciclo
                                count = count + 1
                                break
                            else:
                                pass
                        else:
                            if int(sequence[x-1]) == int(sequence[x+1]):
                                del sequence[x+1]
                                ciclo += ciclo
                                count = count + 1
                                break
                            else:
                                if int(sequence[x+1]) < int(sequence[x-1]):
                                    del sequence[x+1]
                                    ciclo += ciclo
                                    count = count + 1
                                    break
                                else:
                                    del sequence[x]
                                    ciclo += ciclo
                                    count = count + 1
                                    break

                            # print ("count = " + str(count))
                    else:
                        del sequence[x]
                        ciclo += ciclo
                        count = count + 1
                        break
                        # print ("count = " + str(count))

                if x == len(sequence)-1:
                    ciclo = ciclo + 1
                    # print("if final")
                    if int(sequence[x-1]) < int(sequence[x]):
                        pass
                    else:
                        del sequence[x]
                        count = count + 1
                        # print ("count = " + str(count))
                        break

        new_sequence = set(sequence)
        dif_seq = int(len(sequence)) - int(len(new_sequence))
        # print(dif_seq)
        if dif_seq > 0:
            count = count + dif_seq

        # print("count = " + str(count))
        # print(new_sequence)

        if count > 1:
            return False
        else:
            return True


result = almostIncreasingSequence([3, 5, 67, 98, 3])
print(result)
