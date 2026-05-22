#!/usr/bin/env python3
from ex0.factories import (CreatureFactory,
                           FlameFactory,
                           AquaFactory)
from ex1.factories import (HealingCreatureFactory,
                           TransformCreatureFactory)
from ex2.strategies import (BattleStrategy,
                            NormalStrategy,
                            AggressiveStrategy,
                            DefensiveStrategy,
                            InvalidStrategyForCreature)


if __name__ == "__main__":
    def single_battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]
                      ) -> None:
        fighters = [(factory.create_base(), strategy)
                    for factory, strategy in opponents]
        contestants = len(opponents)
        print(f"{contestants} opponents involved")
        for i in range(contestants):
            for j in range(i + 1, contestants):
                creature_a, strategy_a = fighters[i]
                creature_b, strategy_b = fighters[j]
                print("\n* BATTLE *")
                print(f"{creature_a.describe()}\n VS\n{creature_b.describe()}")
                print(" NOW FIGHT!")
                for creature, strategy in [(creature_a, strategy_a),
                                           (creature_b, strategy_b)]:
                    try:
                        result = strategy.act(creature)
                        for action in result:
                            print(action)
                    except InvalidStrategyForCreature as error_message:
                        print(error_message)
                        return

    def main() -> None:
        flame_factory = FlameFactory()
        Aqua_factory = AquaFactory()
        heal_factory = HealingCreatureFactory()
        transform_factory = TransformCreatureFactory()
        agro_factory = AggressiveStrategy()
        normal_strategy = NormalStrategy()
        defensive_strategy = DefensiveStrategy()
        tournament_0 = [(flame_factory, normal_strategy),
                        (heal_factory, defensive_strategy)]
        tournament_1 = [(flame_factory, agro_factory),
                        (heal_factory, defensive_strategy)]
        tournament_2 = [(Aqua_factory, normal_strategy),
                        (heal_factory, defensive_strategy),
                        (transform_factory, agro_factory)]
        print("Tournament 0 (basic)")
        print(" [ Flameling+Normal), (Healing+Defensive) ]")
        print("*** Tournament ***")
        single_battle(tournament_0)
        print("\nTournament 1 (error)")
        print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
        print("*** Tournament ***")
        single_battle(tournament_1)
        print("\nTournament 2 (multiple)")
        print("[ (Aquabub+Normal), (Healing+Defensive), "
              "(Transform+Aggressive) ]")
        print("*** Tournament ***")
        single_battle(tournament_2)

    main()
