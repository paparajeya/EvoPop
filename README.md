## **EvoPop: A Genetic Algorithm for Population Dynamics**  

This project is a Python-based simulation of population growth and shrinkage using a genetic algorithm. It models a world where individuals have varying strengths—**weak**, **normal**, and **strong**—influencing their fitness, survival, and contributions to the gene pool.  

#### **Key Features:**  
- **Initial Population:** The simulation begins with individuals of normal strength, representing a balanced starting point.  
- **Crossover Mechanism:** Offspring are generated through crossover, typically inheriting the "normal" strength of their parents, but with the possibility of divergence.  
- **Mutation Dynamics:** Random mutations introduce variability, creating weak or strong individuals that alter the population's balance.  
- **Population Evolution:** Tracks how the population evolves over multiple generations, observing growth, shrinkage, and the distribution of strengths.  
- **Customisable Parameters:** Adjust mutation rates, population size, and fitness criteria to experiment with different evolutionary scenarios.  

#### **Goals:**  
The project demonstrates the principles of genetic algorithms and evolutionary biology, providing a sandbox for studying genetic variation, fitness-based selection, and the emergence of traits over time.  

#### **How to Use:**  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/paparajeya/EvoPop.git  
   cd EvoPop  
   ```  
2. Install dependencies (if needed):  
   ```bash  
    # Create a virtual environment (optional)
    python3 -m venv .venv
    source .venv/bin/activate

    # Upgrade pip and install requirements
    pip install --U pip
    pip install -r requirements.txt  
   ```  
3. Run the simulation:  
   ```bash  
   python evopop_simulation.py  
   ```  
4. Customise parameters in the script to explore different evolutionary settings.  

#### **Future Plans:**  
- Implement environmental factors affecting survival probabilities.  
- Introduce more nuanced traits and interactions between individuals.  
- Visualise population dynamics using plots or animations.  
