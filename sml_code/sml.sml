fun listByRemovingElement([], element) = [] 
    | listByRemovingElement(headElement :: tailElements, element) =
          if (element = headElement) then
              listByRemovingElement(tailElements, element)
          else
              headElement :: listByRemovingElement(tailElements, element);
  
  fun listByRemovingElements(l, nil) = l
    | listByRemovingElements(l, headElement :: tailElements) =
          listByRemovingElement(listByRemovingElements(l, tailElements), headElement)
  
  fun removeDuplicatesFromList([]) = []
    | removeDuplicatesFromList(headElement :: tailElements) = (headElement :: (removeDuplicatesFromList(listByRemovingElement(tailElements, headElement))));

  
