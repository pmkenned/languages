(* A structure is a module; it consists of a collection of types, exceptions,
 * values and structures (called substructures) packaged together into a logical
 * unit. *)

structure Ford = 
struct
  type car = {make: string, built: int}
  val first = {make = "Ford", built = 1904}
  fun mutate ({make,built}: car) year =
    {make = make, built = year}
  fun built ({built, ...}: car) = built
  fun show (c) = if built c < built first then " - "
                 else "(generic Ford)"
end

structure Year =
struct
  type year = int
  val first = 1900
  val second = 2000
  fun newYear(y: year) = y+1
  fun show(y: year) = Int.toString y
end

structure MutableCar =
struct
  structure C = Ford
  structure Y = Year
end

(* A signature is an interface, usually thought of as a type for a structure: it
 * specifies the names of all the entities provided by the structure as well as
 * the arities of type components, the types of value components, and signatures
 * for substructures. *)

signature MANUFACTURER =
sig
  type car
  val first : car
  val built : car -> int
  val mutate : car -> int -> car
  val show : car -> string
end

signature YEAR =
sig
  eqtype year
  val first : year
  val second : year
  val newYear : year -> year
  val show : year -> string
end

signature MCSIG = 
sig
  structure C : MANUFACTURER
  structure Y : YEAR
end

structure Year1 : YEAR =
struct
  type year = int
  type decade = string
  val first = 1900
  val second = 2000
  fun newYear(y: year) = y+1
  fun leap(y: year) = y mod 4 = 0
  fun show(y: year) = Int.toString y
end

structure MCar : MCSIG = MutableCar

val classic = Year1.show 1968

val antique = MCar.Y.show 1930

(* Can't access components not specified in signature *)
(* val x = Year1.leap(Year1.first) *)

signature ORD =
sig
  type t
  val less : t * t -> bool
end

(* Sort is a parameterized module, with parameter X: ORD *)

functor Sort(X: ORD) =
struct
  fun insert(x, nil) = [x]
    | insert(x, l as y::ys) =
        if X.less(x,y) then x::l
        else y::insert(x,ys)
  fun sort (m : X.t list) = foldl insert nil m
end

structure IntOrd : ORD =
struct
  type t = int
  val less = Int.<
end

(* IntOrd is a structure of the ORD signature. *)
(* Sort is a functor in which the input is a structure of the ORD signature 
 * and the output is a structure with two functions: insert and sort *)
structure IntSort = Sort(IntOrd) (* functor application *)
