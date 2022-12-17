#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>

typedef struct Frog {
  bool hungry;
} Frog;

void day_of_frog(Frog* frog) {
  sleep(2);
  printf("Frog is breathing, moving\n");
  if (frog->hungry) {
    sleep(2);
    printf("Frog is eating grass\n");
  }
  frog->hungry = false;
}

void night_of_frog(Frog* frog) {
  sleep(2);
  printf("Frog is sleeping\n");
  frog->hungry = true;
}

typedef struct Tree {
  bool oxygen;
  Frog* frog;
} Tree;

void day_of_tree(Tree* tree) {
  tree->oxygen = true;
  sleep(2);
  printf("Tree is creating oxygen\n");
  day_of_frog(tree->frog);
}

void night_of_tree(Tree* tree) {
  tree->oxygen = false;
  sleep(2);
  printf("Tree is not creating oxygen\n");
  night_of_frog(tree->frog);
}

typedef struct Sun {
  bool light;
  Tree* tree;
} Sun;

void day(Sun* sun) {
  while (true) {
    sleep(2);
    if (sun->light) {
      printf("Sun is shining\n");
      day_of_tree(sun->tree);
      sun->light = false;
    }
    if (!sun->light) {
      printf("Sun is not shining\n");
      night_of_tree(sun->tree);
      sun->light = true;
    }
  }
}

int main(int argc, char** argv) {
  Frog frog = { true };
  Tree tree = { false, &frog };
  Sun sun = { true, &tree };
  day(&sun);
  return 0;
}
